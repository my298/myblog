from flask import Flask, render_template, request, jsonify, send_file
from musicdl.musicdl import MusicClient
import os
import shutil
import glob
import uuid

app = Flask(__name__)

# 配置
DOWNLOAD_DIR = './my_music'
TEMP_DIR = './musicdl_outputs'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 平台配置
PLATFORMS = {
    '1': {'name': 'QQMusicClient', 'display': 'QQ音乐'},
    '2': {'name': 'NeteaseMusicClient', 'display': '网易云音乐'},
    '3': {'name': 'KugouMusicClient', 'display': '酷狗音乐'},
    '4': {'name': 'KuwoMusicClient', 'display': '酷我音乐'},
    '5': {'name': 'MiguMusicClient', 'display': '咪咕音乐'},
    '6': {'name': 'QianqianMusicClient', 'display': '千千音乐'}
}

# 存储搜索结果中的 song_obj（使用 session_id 或临时存储）
temp_storage = {}

def get_client(platforms):
    """创建音乐客户端"""
    return MusicClient(
        music_sources=platforms if platforms else [],
        init_music_clients_cfg={
            'savedir': TEMP_DIR,
            'search_size_per_source': 30,
            'timeout': 30,
        },
        clients_threadings={},
        requests_overrides={},
        search_rules={}
    )

def search_songs(keyword, platforms):
    """搜索歌曲"""
    client = get_client(platforms)
    results = client.search(keyword)
    
    all_songs = []
    seen = set()
    
    for platform, songs in results.items():
        platform_display = next(
            (p['display'] for p in PLATFORMS.values() if p['name'] == platform),
            platform.replace('MusicClient', '')
        )
        
        for song in songs:
            song_key = f"{song.song_name}|{song.singers}"
            if song_key in seen:
                continue
            seen.add(song_key)
            
            file_ext = ''
            if hasattr(song, 'ext') and song.ext:
                file_ext = song.ext.upper()
            elif song.download_url:
                file_ext = song.download_url.split('.')[-1].split('?')[0].upper()
            
            # 生成临时ID存储 song_obj
            temp_id = str(uuid.uuid4())[:8]
            temp_storage[temp_id] = song
            
            all_songs.append({
                'temp_id': temp_id,
                'platform': platform_display,
                'name': song.song_name,
                'singers': song.singers,
                'album': song.album or '未知专辑',
                'duration': song.duration,
                'format': file_ext or 'MP3',
                'file_size': song.file_size
            })
    
    return all_songs

def download_song(song_obj, song_name, singers):
    """下载单首歌曲 - 使用 song_obj 所属的平台"""
    # 获取歌曲来源平台
    source_platform = getattr(song_obj, 'source', None)
    if source_platform:
        # 使用歌曲来源平台创建客户端
        client = get_client([source_platform])
    else:
        # 如果无法获取来源，尝试从 song_obj 的类名推断
        class_name = song_obj.__class__.__name__
        # 尝试找到对应的平台
        matched_platform = None
        for p in PLATFORMS.values():
            if p['name'] in class_name:
                matched_platform = p['name']
                break
        if matched_platform:
            client = get_client([matched_platform])
        else:
            # 最后尝试使用酷狗作为默认
            client = get_client(['KugouMusicClient'])
    
    client.download([song_obj])
    
    downloaded_files = []
    if os.path.exists(TEMP_DIR):
        for root, dirs, files in os.walk(TEMP_DIR):
            for file in files:
                if file.endswith(('.mp3', '.flac', '.m4a', '.wav', '.aac', '.ogg')):
                    src_path = os.path.join(root, file)
                    # 生成友好的文件名
                    safe_name = f"{song_name} - {singers}".replace('/', '_').replace('\\', '_').replace(':', '_')
                    ext = file.split('.')[-1]
                    dst_path = os.path.join(DOWNLOAD_DIR, f"{safe_name}.{ext}")
                    
                    counter = 1
                    name_without_ext = safe_name
                    while os.path.exists(dst_path):
                        dst_path = os.path.join(DOWNLOAD_DIR, f"{name_without_ext}_{counter}.{ext}")
                        counter += 1
                    
                    shutil.copy2(src_path, dst_path)
                    downloaded_files.append(dst_path)
    
    # 清理临时文件
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    for pkl_file in glob.glob('*.pkl'):
        try:
            os.remove(pkl_file)
        except:
            pass
    
    return downloaded_files[0] if downloaded_files else None

@app.route('/')
def index():
    """首页"""
    return render_template('index.html', platforms=PLATFORMS)

@app.route('/search', methods=['POST'])
def search():
    """搜索接口"""
    data = request.get_json()
    keyword = data.get('keyword', '').strip()
    platform_keys = data.get('platforms', [])
    
    if not keyword:
        return jsonify({'error': '请输入歌曲名'}), 400
    
    # 获取选中的平台
    if not platform_keys:
        platforms = []
    else:
        platforms = [PLATFORMS[k]['name'] for k in platform_keys if k in PLATFORMS]
    
    try:
        songs = search_songs(keyword, platforms)
        return jsonify({'songs': songs})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['POST'])
def download():
    """下载接口 - 直接使用存储的 song_obj，不再重新搜索"""
    data = request.get_json()
    temp_id = data.get('temp_id')
    
    if not temp_id or temp_id not in temp_storage:
        return jsonify({'error': '歌曲信息已过期，请重新搜索'}), 400
    
    try:
        song_obj = temp_storage[temp_id]
        song_name = song_obj.song_name
        singers = song_obj.singers
        
        # 下载
        file_path = download_song(song_obj, song_name, singers)
        
        # 清理存储
        del temp_storage[temp_id]
        
        if file_path and os.path.exists(file_path):
            return send_file(
                file_path, 
                as_attachment=True, 
                download_name=os.path.basename(file_path),
                mimetype='audio/mpeg'
            )
        else:
            return jsonify({'error': '下载失败，请重试'}), 500
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)