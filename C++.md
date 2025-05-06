# C++
### 入门
#### 最简单的C++程序
```
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++!" << endl;
    return 0;
}
```
最基本的：
```
#include <iostream>

using namespace std;
<!-- 一般会有
#include <string>
#include <cmath>
等头文件
 -->
```
#### 变量
##### 基本数据类型  
C++提供多种数据类型来存储不同种类的数据：
```
int age = 20;
float height = 1.75;
char grade = 'A';
bool isPassed = true;
string s; //需要#include <string>头文件
```
##### 不同类型字节大小
int float :4  
double :8  
char bool :1 

##### 关于输出(cout)
```
int a = 5;
double pi = 3.14;
char letter = 'Z';
bool isOk = false;

cout << "a = " << a << endl;
cout << "pi = " << pi << endl;
cout << "letter = " << letter << endl;
cout << "isOk = " << isOk << endl;
```
##### 关于输入
```
int age;
cout << "请输入你的年龄：";
cin >> age;
cout << "你输入的年龄是：" << age << endl;
```
对于多个变量输入有：
```
int a, b;
cin >> a >> b;
```
#### 字符串
```
#include <string>
using namespace std;

string s = "hello";
cout << s << endl;

cin >> s;        // 输入一个单词（不含空格）
getline(cin, s); // 输入一整行（含空格）
```
关于字符串函数有：
（1）获取长度 : s.length()
```
string s = "hello";
cout << s.length();  // 输出 5
```
(2)判断字符串是否为空: s.empty()
```
string s = "";
if (s.empty()) {
    cout << "字符串是空的";
}
```
(3)拼接字符串 ——s.append(" ")
```
string s = "hello";
s.append(" world");   // 等同于 s += " world";
cout << s;  // hello world
```
(4) substr(pos, len)
截取子串，从 pos 开始，取 len 个字符
```
string s = "abcdef";
string sub = s.substr(2, 3);  // 从下标2开始取3个字符 -> "cde"
```
(5) find(str)
查找子串首次出现的位置，找不到返回 string::npos
```
string s = "hello world";
int pos = s.find("world");  // pos = 6
if (pos != string::npos) {
    cout << "找到了";
}
```
(6) rfind(str)
从后往前找子串位置（仍然返回的是下标）
```
string s = "abcabc";
int pos = s.rfind("a");  // pos = 3（最后一个 a 的位置）
```
(7) insert(pos, str)
在指定位置插入子串
```
string s = "helloworld";
s.insert(5, " ");  // 在第5个字符后插入空格
cout << s;  // hello world
```
(8) erase(pos, len)
删除从 pos 开始的 len 个字符
```
string s = "hello world";
s.erase(5, 1);  // 删除第6个字符（空格）
cout << s;  // helloworld
```
(9) replace(pos, len, str)
替换从 pos 开始的 len 个字符为 str
```
string s = "I like apples";
s.replace(7, 6, "bananas");  // 替换“apples”为“bananas”
cout << s;  // I like bananas
```
(10) compare(str)
比较两个字符串（返回值含义和 strcmp 一样）
```
string a = "abc";
string b = "abd";
if (a.compare(b) < 0) 
cout << "a < b";
```
(11) getline(cin, str)
读取整行输入（包括空格）
```
string s;
getline(cin, s);  // 输入："hello world"  → s = "hello world"
```