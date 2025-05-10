# JavaScript
### JavaScript 的三种运行方式：

* **1. 嵌入 HTML 页面内部**  
  在 `<script>` 标签中直接编写代码：
  ```
  <script>
    alert("Hello, world!");
  </script>
  ```

* **2. 引入外部 .js 文件**  
  通过 `src` 属性引入外部 JS 文件：
  ```
  <script src="script.js"></script>
  ```

* **3. 在控制台运行**  
  打开浏览器开发者工具（Chrome 按 `F12`）→ 进入 **Console** 面板 → 直接输入 JS 代码执行。

### 变量与数据
<span style="margin-left:1em "> **1.JavaScript 里可以用三种方式声明变量：**</span>

* **var**（老语法，了解即可）

* **let**（推荐）

* **const**（用于声明常量）

<span style="margin-left:1em">**2. 常见的数据类型**
</span>

* 字符串String
* 数字Number
* 布尔 Boolean
* 空值 null
* 未定义 undefined
* 对象 Object
* 数组 Array

<span style="margin-left:1em">**3. 常用运算符分类**
</span>

* 算术运算符(+ - * \ % **)
    ** : 幂运算符 2 ** 3=8
* 赋值运算符
* 比较运算符 (===严格相等)
* 逻辑运算符

### 条件语句
* if语句
* if...else语句
* if ...else if...else

### 循环
* for循环
* while 循环
* do...while循环
* for...of 循环
* for...in 循环
  
***break:跳出整个循环***
***continue：跳出当前循环***

### 函数
#### 函数声名方式
(1)普通函数声明
```
function greet() {
  console.log("你好，澈");
}
greet();  // 调用函数
```
(2)带参数的函数
```
function greet(name) {
  console.log("你好，" + name);
}
greet("舟舟");  // 输出：你好，舟舟
```
(3)返回值
```
function add(a, b) {
  return a + b;
}
let result = add(3, 5);
console.log(result);  // 输出 8
```
(4) **函数表达式**
```
const sayHi = function(name) {
  console.log("Hi, " + name);
};
sayHi("澈");
```
与其他函数的区别：
* 没有函数名
* 必须在定义后才能调用 即没有函数提升

(5) **箭头函数**
```
const add = (a, b) => {
  return a + b;
};
```
简化写法：
* 只有一个表达式
  ```
  const add = (a, b) => a + b;
  ```
* 只有一个参数(可以省略括号)
  ```
  const square = x => x * x;
  ```
箭头函数与普通函数的区别：
* 普通函数：（1）this指针指向调用者（2）可以提升 （3）推荐用作方法
* 箭头函数：（1）this指针指向上一级调用者 （2）不可以提升 （3） 不推荐用作方法，因为没有this指针
### 数组
#### 数组的创建
```
let arr1 = [1, 2, 3];
let arr2 = ["澈", "舟舟", "星河"];
let arr3 = [];  // 空数组
```
#### 访问数组中的元素
```
let names = ["澈", "舟舟"];
console.log(names[0]);  // 输出：澈
console.log(names[1]);  // 输出：舟舟
```
* 索引从0开始。
* names[2]会返回undefined，因为不存在
#### 修改数组元素
```
names[1] = "星河";  // 把 "舟舟" 改成 "星河"
```
#### 数组常用属性和方法
* arr.length —— 返回数组长
* arr.pop() —— 删除最后一个元素
* arr.shift() —— 删除第一个元素
* arr.unshift(value) —— 在开头添加元素
* arr.push(value) —— 在末尾添加元素
* arr.indexOf(value) —— 查找元素位置 ，没找到返回-1
* arr.includes(value) —— 查看是否包含元素，返回true或者false
* for, for...of,forEach() —— 遍历数组
#### 数组遍历的方法
##### 普通遍历
(1) for 循环
```
const arr = [1, 2, 3];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```
(2)for...of循环
```
for (const item of arr) {
  console.log(item);
}
```
##### 功能性遍历
(3)forEach()
对数组每个元素执行回调函数，没有返回值
```
arr.forEach((item, index, array) => {
  console.log(item, index);
});
```
(4)map()
对每个元素执行回调，返回新数组
```
const doubled = arr.map(item => item * 2);
// [2, 4, 6]
```
(5)filter()
返回满足条件的元素组成的新数组
```
const evens = arr.filter(item => item % 2 === 0);
// [2]
```
(6)reduce()
将数组缩减为单个值
```
const sum = arr.reduce((acc, curr) => acc + curr, 0);
// 6
```
(7)reduceRight()
从右向左执行reduce
```
const flattened = [[0,1], [2,3]].reduceRight((a, b) => a.concat(b));
// [2, 3, 0, 1]
```
##### 查找方法
(8) find()
返回第一个满足条件的元素
```
const found = arr.find(item => item > 1);
// 2
```
(9)findIndex()
返回第一个满足条件的元素的索引
```
const index = arr.findIndex(item => item === 2);
// 1
```
some()
检查是否有元素满足条件
```
const hasEven = arr.some(item => item % 2 === 0);
// true
```
every()
检查所有元素是否满足条件
```
const allEven = arr.every(item => item % 2 === 0);
// false
```

### 对象
#### 对象创建的方法
（1）对象字面量
```
let person = {
  name: "澈",
  age: 22,
  isCool: true
};
```
(2)访问对象属性
```
console.log(person.name);   // 澈
console.log(person["age"]); // 22
```
* 对象访问用 .
* 指针访问用 ->
  
(3)修改和添加属性
```
person.age = 23;            // 修改属性
person.hobby = "driving";   // 添加新属性
```
(4) 删除属性
```
delete person.isCool;
```
#### 遍历对象属性
```
const person = {
  name: 'Alice',
  age: 25,
  job: 'Engineer'
};
for (let key in person) {
  console.log(key + ": " + person[key]);
}
```
* key : 属性名
* person[key] ：属性值
* for...in 用来遍历对象属性名
* 用person[key]获取对应值
  
对于以上代码有
1. 第一次迭代：`key = 'name'` → 输出 `"name: Alice"` 
2. 第二次迭代：`key = 'age'` → 输出 `"age: 25"` 
3. 第三次迭代：`key = 'job'` → 输出 `"job: Engineer"` 

#### 方法：对象中的函数
对象可以包含函数，称为方法
```
let person = {
  name: "澈",
  sayHi: function() {
    console.log("你好，我是" + this.name);
  }
};

person.sayHi();  // 调用方法
```
#### this 在对象中的使用
* this 是一个关键字，它指向当前调用该函数的对象。
* 在对象的方法中，this 通常指向该对象本身。
```
let person = {
  name: "澈",
  greet: function() {
    console.log("你好，我是 " + this.name);
  }
};

person.greet();  // 输出：你好，我是 澈
```
当greet()被调用时，this指向person，因此输出 person. name.

* 1.3 this 在不同情况下的表现：

   a. 在对象方法中，this 指向该对象。

  b. 在普通函数中，this 指向全局对象（在浏览器中是 window，在严格模式下是 undefined）。

   c.在箭头函数中，this 会继承自外部函数的 this，这就是箭头函数与普通函数的一个重要区别。
```
普通函数：
let person = {
  name: "澈",
  greet: function() {
    console.log("你好，我是 " + this.name);
    setTimeout(function() {
      console.log(this.name);  // 普通函数中的 this 指向全局对象
    }, 1000);
  }
};

person.greet();  // 输出：你好，我是 澈，然后输出 undefined
```
greet()属于对象，所以this指向person
回调函数属于普通函数，所以this指向全局对象（window）
```
箭头函数
let person = {
  name: "澈",
  greet: function() {
    console.log("你好，我是 " + this.name);
    setTimeout(() => {
      console.log(this.name);  // 箭头函数中的 this 继承自 greet 函数
    }, 1000);
  }
};

person.greet();  // 输出：你好，我是 澈，然后输出 澈
```
greet()属于对象，所以this指向person；
箭头函数不绑定自己的this，指向外层的this，这里的外层即是greet(),所以this指向person
#### 对象嵌套
```
let company = {
  name: "澈科技",
  address: {
    city: "北京",
    street: "朝阳区"
  },
  employees: [
    { name: "舟舟", role: "开发" },
    { name: "星河", role: "设计" }
  ]
};

console.log(company.address.city); // 输出：北京
console.log(company.employees[0].name); // 输出：舟舟
```
* company.address 是一个嵌套对象，你可以通过 company.address.city 获取它的属性。

* company.employees 是一个数组，里面存放着多个对象。

#### 构造函数

(1)构造函数的写法

```
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function() {
    console.log("你好，我是 " + this.name + "，今年 " + this.age + " 岁");
  };
}

let person1 = new Person("澈", 22);
let person2 = new Person("舟舟", 21);

person1.greet();  // 输出：你好，我是 澈，今年 22 岁
person2.greet();  // 输出：你好，我是 舟舟，今年 21 岁
```
* Person 是一个构造函数，它用来创建一个具有 name、age 和 greet 方法的对象。

* 使用 new 关键字可以创建多个 Person 对象。

* this 在构造函数中指向新创建的对象。



（2）构造函数的注意点

* 构造函数的首字母通常大写（这是约定俗成的规范）。

* 使用 new 关键字时，JavaScript 会自动把构造函数中的 this 指向一个新的对象。

* 如果不使用 new，构造函数的 this 会指向全局对象（在浏览器中是 window）。

### 事件
#### 关于事件
事件是用户与网页交互时触发的行为，例如点击、键盘输入、表单提交等。
#### 事件绑定
（1）通过HTML属性绑定事件（旧写法，不推荐）
```
<button onclick="alert('按钮被点击了！')">点击我</button>
```
（2）DOM属性绑定（早期写法，也不推荐）
```
const btn = document.querySelector('#btn');//获取元素
btn.onclick = function () {
  alert('clicked');
};
```
缺点：只能绑定一个函数，后面绑定的会覆盖前一个
(3)现代写法（推荐）
```
const btn = document.querySelector('#btn');
btn.addEventListener('click', function () {
  alert('clicked');
});
```
优点：（1）可以绑定多个处理器
（2）支持事件冒泡和捕获
#### 获取对象
（1）querySelector()——返回单个元素
 (2)querySelectorAll() —— 返回NodeList
（3）推荐的 DOM 操作方法

现代浏览器支持一些更加高效和简洁的 DOM 操作方法，例如：

（1）element.closest(selector)：获取最近的匹配的祖先元素（包括自身）。
```
<body>
    <ul>
        <li><a href="#">111</a></li>
        <li><a href="#">222</a></li>
        <li><a href="#">333</a></li>
        <li><a href="#">444</a></li>
    </ul>
    <script>
        document.querySelector("ul").addEventListener("click",(event) => {
  const link = event.target.closest("a"); // 确保点击的是 <a> 或其子元素
  if (!link) return; // 如果不是 <a>，直接退出

  event.preventDefault(); // 阻止默认跳转（因为 href="#")
  console.log("点击了链接，位置：", link.parentElement); // 输出对应的 <li>
});
    </script>
</body>

```
link:得到具体的a元素
link.parentElement:得到link的父元素，也就是li
（2）element.matches(selector)：检查当前元素是否匹配指定的 CSS 选择器。
```
// 检查点击的是否是一个带有特定 class 的 <a>
document.querySelector("ul").addEventListener("click", (event) => {
  if (event.target.matches("a.active")) { // 必须是 <a class="active">
    event.preventDefault();
    console.log("点击了高亮链接");
  }
});
```
#### 事件监听
##### 绑定事件
```
let button = document.querySelector(".myButton");
button.addEventListener("click", function() {
  alert("按钮被点击了！");
});
```
addEventListener可以在一个元素绑定多个事件，而不会覆盖前面的
##### 移除事件
```
function handleClick() {
  alert("按钮被点击了！");
}
let button = document.querySelector(".myButton");
button.addEventListener("click", handleClick);

// 移除事件
button.removeEventListener("click", handleClick);
```
常见的事件类型
* click ——点击
* dblclick —— 双击
* mouseover —— 鼠标悬停
* mouseout —— 鼠标离开
* keydown —— 按下键盘按键
* keyup —— 键盘按键释放
* focus —— 获得焦点
* blur ——失去焦点
* submit—— 提交表单
* change —— 值改变（表单事件）
* input —— 用户输入时立即触发

#### 事件对象
事件触发时，会自动生成一个事件对象，这个对象包含了事件的详细信息。常用的属性有：

* event.target：触发事件的元素。

* event.type：事件的类型（如：click）。

* event.preventDefault()：阻止事件的默认行为。

* event.stopPropagation()：阻止事件的冒泡。
```
let button = document.querySelector(".myButton");
button.addEventListener("click", function(event) {
  console.log(event.target);  // 输出触发事件的元素
  console.log(event.type);    // 输出事件类型：click
  event.preventDefault();    // 阻止默认行为（如链接跳转）
});
```
#### 事件监听器的现代写法
（1）使用箭头函数
```
document.querySelector(".myButton").addEventListener("click", (event) => {
  alert("按钮被点击了！");
});
```

#### 事件委托
事件委托是指将事件绑定到父元素而不是子元素上，利用事件冒泡机制来处理多个子元素的事件。这样可以提高性能，减少 DOM 元素的绑定。
```
<ul id="myList">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
<script>
  const list = document.getElementById('myList');
  list.addEventListener('click', function(event) {
    if (event.target.tagName === 'LI') {
      alert('List item clicked: ' + event.target.textContent);
    }
  });
</script>
```
`event.target`:表示实际被点击的元素
`event.target.textContent`:返回被点击元素及其后代元素的所有纯文本内容

在这个例子中，我们没有为每个按钮绑定事件，而是将事件绑定到父元素 parentDiv 上，然后通过 event.target 来判断点击的是否是 button 元素。

这种方式可以在动态添加子元素时，仍然能够正常工作。

##### 使用once,capture,passive选项
addEventListener 方法有一些额外的选项，允许你更细粒度地控制事件监听的行为。

once：指定事件监听器在触发一次后就被移除。

capture：指定事件是否在捕获阶段触发（默认为冒泡阶段）。

passive：告知浏览器事件不会调用 preventDefault()，有助于优化滚动等性能密集型操作。

(1)使用once
```
document.querySelector(".myButton").addEventListener("click", () => {
  alert("按钮被点击了！");
}, { once: true });
```
once: true :表示事件只会触发一次，之后自动移除事件监听器。

（2）使用capture，passive
```
document.querySelector(".myButton").addEventListener("click", () => {
  alert("按钮被点击了！");
}, { capture: true, passive: true });
```
capture: true:表示在捕获阶段触发；
passive: true：提示浏览器事件不会调用 preventDefault()，因此优化滚动等性能密集型操作
### 异步编程
#### 回调函数(最早的)
```
setTimeout(function() {
  console.log("异步任务完成");
}, 1000);
```
#### Promise(推荐使用)
Promise 是对回调函数的一种改进。它可以链式调用，避免了回调地狱。
```
let promise = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve("异步任务完成");
  }, 1000);
});

promise.then(function(result) {
  console.log(result);  // 输出：异步任务完成
}).catch(function(error) {
  console.log(error);
});
``` 
resolve 表示操作成功，reject 表示操作失败。

.then() 用来处理成功的结果，.catch() 用来处理错误。

#### async/await(最新写法，推荐)
async/await 是 Promise 的语法糖，它使得异步代码看起来像同步代码，简洁且易于理解。
```
async function fetchData() {
  let promise = new Promise(function(resolve, reject) {
    setTimeout(() => resolve("异步任务完成"), 1000);
  });

  let result = await promise;  // 等待 Promise 完成
  console.log(result);  // 输出：异步任务完成
}

fetchData();
```
async 修饰函数，表示该函数是一个异步函数。

await 用来等待 Promise 的结果，类似于同步操作。

await 只能在 async 函数中使用。

#### 异步编程中的错误处理
##### 使用 try...catch 捕获异常（async/await）
```
async function fetchData() 
{
  try 
  {
    let promise = new Promise(function(resolve, reject) 
    {
      setTimeout(() => reject("出错了！"), 1000);
    });

    let result = await promise;  // 等待 Promise 完成
    console.log(result);
  } catch (error) 
  {
    console.log(error);  // 输出：出错了！
  }
}

fetchData();
```
new Promise(function(resolve, reject)
* new Promise((resolve) => { ... })	✅ 合法	常用，适合只需要成功的情况
* new Promise((_, reject) => { ... })	✅ 合法	罕见，适合只处理错误（不建议这样）
* new Promise(() => { ... })	✅ 合法	不推荐，会导致 Promise 永远 pending
* new Promise((resolve, reject) => { ... })	✅ 合法	标准写法，推荐
使用 try...catch 结构来捕获异常。

如果 await 等待的 Promise 被拒绝，错误将被 catch 捕获。
该代码运行步骤：
```
fetchData() →
  创建 Promise →
    await 暂停 →
      1秒后 reject →
        Promise 被拒绝 →
          抛出异常 →
            try...catch 捕获 →
              打印错误
```
##### Promise.all() 和 Promise.race()

Promise.all() 和 Promise.race() 是处理多个 Promise 的两种常见方法。
(1)Promise.all()
Promise.all() 用于并行执行多个异步操作，并在所有操作都完成时执行回调。
```
let promise1 = new Promise((resolve) => setTimeout(resolve, 1000, '任务1'));
let promise2 = new Promise((resolve) => setTimeout(resolve, 2000, '任务2'));

Promise.all([promise1, promise2]).then((results) => {
  console.log(results);  // 输出：["任务1", "任务2"]
});

Promise.all()
```
Promise.all() 会等待所有的 Promise 都成功，返回一个包含所有结果的数组。

##### Promise.race() 
用于等待多个 Promise 中的第一个完成的操作。
（1）任务都是resolve
```
let promise1 = new Promise((resolve) => setTimeout(resolve, 1000, '任务1'));
let promise2 = new Promise((resolve) => setTimeout(resolve, 500, '任务2'));

Promise.race([promise1, promise2]).then((result) => {
  console.log(result);  // 输出：任务2
});
```
Promise.race() 会返回第一个完成的 Promise。
（2）任务都是reject
```
let promise1 = new Promise((_, reject) => setTimeout(reject, 1000, '任务1失败'));
let promise2 = new Promise((_, reject) => setTimeout(reject, 500, '任务2失败'));

Promise.race([promise1, promise2]).then(
  (result) => {
    console.log('成功:', result);
  },
  (error) => {
    console.log('失败:', error);  // 输出：失败: 任务2失败
  }
);
```
(3)混合resolve和reject
```
let promise1 = new Promise((_, reject) => setTimeout(reject, 1000, '任务1失败'));
let promise2 = new Promise((resolve) => setTimeout(resolve, 500, '任务2成功'));

Promise.race([promise1, promise2]).then(
  (result) => {
    console.log('成功:', result);  // 输出：成功: 任务2成功
  },
  (error) => {
    console.log('失败:', error);
  }
);
```
Promise.race() 谁先有结果（resolve 或 reject），就以那个为准。

## 模块化开发
### 导出(export)
（1）命名导出
命名导出允许你导出多个变量、函数或类。每个导出的内容都需要指定名称，导入时必须使用相同的名称。
```
// file1.js
export const myVar = 'Hello, world!';
export function myFunction() {
  console.log('This is a function.');
}
export class MyClass {
  constructor() {
    this.name = 'MyClass';
  }
}

```
（2）默认导出()
默认导出允许你导出一个单一的值，通常是一个类、对象或函数。导入时可以使用任何名称。
```
// file1.js
export default function() {
  console.log('This is the default export!');
}
```
(3)重命名导出
在导出时，你可以选择重新命名变量、函数或类。
```
// file1.js
const myVar = 'Hello, world!';
export { myVar as greeting };
```
(4)一次性导出多个内容
你可以将多个内容一次性导出，避免多次使用 export 语法。
```
// file1.js
const myVar = 'Hello, world!';
const myFunction = () => {
  console.log('This is a function.');
};

export { myVar, myFunction };
```
### 导入
（1）导入命名导出的内容
导入时，使用花括号包裹你需要的导出内容。导入的名称必须与导出的名称一致。
```
// file2.js
import { myVar, myFunction } from './file1.js';

console.log(myVar);       // Hello, world!
myFunction();             // This is a function.
```
(2)导入默认导出的内容
导入默认导出时，你可以为其指定任何名称。
```
// file2.js
import myFunction from './file1.js';

myFunction();  // 输出：This is the default export!
```
(3)导入所有内容（Import All）
你可以使用 * as 导入模块中的所有导出内容，并将它们作为一个对象来使用
```
// file2.js
import * as myModule from './file1.js';

console.log(myModule.myVar);     // Hello, world!
myModule.myFunction();           // This is a function.
```
(4) 导入并重命名内容
你可以导入时重命名内容，特别是当导出的名称与你的本地变量名冲突时。
```
// file2.js
import { myVar as greeting } from './file1.js';

console.log(greeting);  // Hello, world!
```
(5)动态导入
可以使用 import() 函数来动态加载模块。import() 返回一个 Promise，适合按需加载模块或实现懒加载。
* Promise.then()链式调用
```
// 动态导入模块
import('./file1.js')
  .then(module => {
    console.log(module.myVar);  // Hello, world!
    module.myFunction();        // This is a function.
  })
  .catch(err => console.error('模块加载失败:', err));
```
这里的err表示catch捕获的错误对象
* async / await方式
```
// app.js
async function loadModule() {
  try {
    const mathModule = await import('./math.js');
    console.log(mathModule.pi);  // 输出：3.14159
  } catch (err) {
    console.error('模块加载失败:', err);
  }
}

loadModule();
```
（6）默认导出与命名导出同时使用
一个模块可以同时使用 默认导出 和 命名导出。默认导出适用于你想要作为模块主内容的情况，而命名导出适用于其他附加的内容。
```
// file1.js
export const myVar = 'Hello, world!';
export default function() {
  console.log('This is the default export!');
}
```
```
// file2.js
import myFunction, { myVar } from './file1.js';

console.log(myVar);       // Hello, world!
myFunction();             // This is the default export!
```
#### 模块的扩展名
在浏览器环境中，模块文件的扩展名通常是 .js。
```
<script type="module">
  import { pi } from './math.js';
  console.log(pi);  // 输出：3.14159
</script>
```
在浏览器中，<script type="module"> 会告诉浏览器该文件是一个模块。浏览器会自动处理模块间的依赖关系。
