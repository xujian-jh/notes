# [lit-html] 是一个模板库

- 采用 [template literals] 模板字面量（JavaScript 语法），编辑 html 模板
- 借用 `<template>` 元素，最终实例化
- 将 Web UI 表达为数据

## [NPM] 安装

- 工程目录，配置文件设置依赖，然后下载
```json
{
  ....,
  "dependencies": {
    "lit-html": "^1.0.0"
  },
  "engines": {
    "node": ">=7.6.0"
  }
}
```
```
npm install
```

## 一个例子

```js
// Import lit-html
import {html, render} from 'lit-html';

// Define a template
let myTemplate = (data) => html`
  <h1>${data.title}</h1>
  <p>${data.body}</p>`;

// Render the template to the document
const result = myTemplate({title: 'Hello', body: 'lit-html is cool'});
render(result, document.body);
```
- `import` 语句仅适用于模块脚本（`<script type="module">`）
  - 浏览器仅支持按路径导入
  - 如果使用将包名称转换为路径的工具，则可以按包名称导入
```js
<script type="module">
  import {html, render} from './node_modules/lit-html/lit-html.js';
  ...
</script>
```
- lit-html 模板，即带标记的模板字面量函数
  - `html` 标记
  - 反引号（``）模板字面量，适用多行
  - 占位符 `${}`，花括号内插入 JavaScript 语句
  - lit-html is lazily rendered.
  - lit-html 模板返回一个对象 `TemplateResult`
- 填充数据，对象 `TemplateResult` 实例化
- `render()` 函数实际上创建 DOM 节点并将它们附加到 DOM 树

## 模板编辑方法

1. 呈现静态 HTML
- 仅仅使用带标记的模板字面量
```js
import {html, render} from 'lit-html';

// Declare a template
const myTemplate = html`<div>Hello World</div>`;

// Render the template
render(myTemplate, document.body);
```
2. 呈现动态文本内容
- 使用带标记的模板字面量
- 在模板字面量中使用占位符 `${expression}` 绑定
- 在数据发生变化时调用模板函数
- 当您调用时 render，lit-html 仅更新自上次渲染以来已更改的部分
```js
import {html, render} from 'lit-html';

// Define a template function
const myTemplate = (name) => html`<div>Hello ${name}</div>`;

// Render the template with some data
render(myTemplate('world'), document.body);

// ... Later on ... 
// Render the template with different data
render(myTemplate('lit-html'), document.body);
```
3. 使用表达式
- 绑定可以包含任何类型的 JavaScript 表达式
```js
const myTemplate = (subtotal, tax) => html`<div>Total: ${subtotal + tax}</div>`;
const myTemplate2 = (name) => html`<div>${formatName(name.given, name.family, name.title)}</div>`;
```
4. 绑定关键属性（attributes）
- 默认情况下，属性值中的表达式会创建属性绑定
```js
// set the class attribute
const myTemplate = (data) => html`<div class=${data.cssClass}>Stylish text.</div>`;

```
- 使用 `?` 前缀作为布尔属性绑定。如果表达式求值为 `truthy`，则添加该属性；如果求值为 `falsy`，则删除该属性
```js
const myTemplate2 = (data) => html`<div ?disabled=${!data.active}>Stylish text.</div>`;
```
5. 绑定属性（properties）
- 使用 `.` 前缀和属性名称绑定到节点的 JavaScript 属性
```js
const myTemplate3 = (data) => html`<my-list .listItems=${data.items}></my-list>`;
```
6. 添加事件侦听器
- 使用 `@` 前缀和事件名称添加事件侦听器
```js
const myTemplate = () => html`<button @click=${clickHandler}>Click Me!</button>`;
```
7. 嵌套模板
- 
```js
const myHeader = html`<h1>Header</h1>`;
// some complex view
const myListView = (items) => html`<ul>...</ul>`;

const myPage = (data) => html`
  ${myHeader}
  ${myListView(data.items)}
`;
```
8. 条件模板
- 三元表达式是添加内联条件的好方法
```js
html`
  ${user.isloggedIn
      ? html`Welcome ${user.name}`
      : html`Please log in`
  }
`;
```
- 带有 if 语句的条件句
```js
getUserMessage() {
  if (user.isloggedIn) {
    return html`Welcome ${user.name}`;
  } else {
    return html`Please log in`;
  }
}

html`
  ${getUserMessage()}
`
```
9. 重复模板
- 使用 `Array.map` 将数据列表转换为模板列表
```js
html`
  <ul>
    ${items.map((item) => html`<li>${item}</li>`)}
  </ul>
`;
```
- 使用循环语句重复模板
```js
const itemTemplates = [];
for (const i of items) {
  itemTemplates.push(html`<li>${i}</li>`);
}

html`
  <ul>
    ${itemTemplates}
  </ul>
`;
```
- `repeat(items, keyFunction, itemTemplate)`
  - items 是一个数组
  - keyFunction 是一个函数，它将一个项目作为参数，并返回该项目的保证唯一键
  - itemTemplate 是一个模板函数，它将项及其当前索引作为参数，并返回一个 TemplateResult
  - repeat 指令，根据键值更新（重新排序）
```js
const employeeList = (employees) => html`
  <ul>
    ${repeat(employees, (employee) => employee.id, (employee, index) => html`
      <li>${index}: ${employee.familyName}, ${employee.givenName}</li>
    `)}
  </ul>
`;
```
10. 缓存模板结果：缓存指令















[lit-html]: https://lit-html.polymer-project.org/guide

[template literals]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals

[NPM]: https://www.npmjs.com/package/lit-html

