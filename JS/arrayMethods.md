阅读笔记：合理使用 [Array] ，为开发提供巨大帮助，有机会多研究。

[Array]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

# Array.map()

```js
let newArray = oldArray.map((value, index, array) => {
  ...
});
```

- 助记符 map ( morph Array piece-by-piece )，按条件映射
- 改变数组的每个成员，生成新数组
- 数组成员个数维持不变

```js
[1, 4, 6, 14, 32, 78].map(val => val * 10)
// the result is: [10, 40, 60, 140, 320, 780]
```

# Array.filter()

```js
[1, 4, 6, 14, 32, 78].filter(val => val > 10)
// the result is: [14, 32, 78]
```

- 按条件过滤
- 给定数组中的每个满足条件的值，生成新数组
- 数组成员个数维持不变或减少

```js
[1, 4, 6, 14, 32, 78].map(val => val > 10)
// the result is: [false, false, false, true, true, true]
```

# Array.reduce()

#### 语法：

```js
let finalVal = oldArray.reduce( callback() [, initialValue] )
```

#### 按条件缩减

- 数组成员执行 reducer 函数（自定义），累积生成单个输出值
- 第一个参数 callback() 回调函数
  1. accumulator 累加器，累加回调的返回值
  2. currentValue 当前值
  3. currentIndex 源数组索引（可选）
  4. array 源数组（可选）
  - 注意：源数组索引 0 表示 initialValue ，数组成员从索引 1 开始
- 第二个参数（可选） initialValue 初始值
  - 如果数组为空并且 initialValue 未提供，抛出 TypeError
  - 如果数组只有一个成员（无论位置如何）并且 initialValue 未提供，或者如果 initialValue 提供但是数组为空，则返回单个值
  - 提供 initialValue 通常更安全

#### 举例

1. 应用场景：数字求和
```js
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

2. 应用场景：对象求和（必须提供初始值）
```js
var initialValue = 0;
var sum = [{x: 1}, {x: 2}, {x: 3}].reduce(
    (accumulator, currentValue) => accumulator + currentValue.x
    ,initialValue
);

console.log(sum) // logs 6
```

3. 应用场景：对象计数
```js
var names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'];

var countedNames = names.reduce(function (allNames, name) { 
  if (name in allNames) {
    allNames[name]++;
  }
  else {
    allNames[name] = 1;
  }
  return allNames;
}, {});
// countedNames is:
// { 'Alice': 2, 'Bob': 1, 'Tiff': 1, 'Bruce': 1 }
```

4. 应用场景：分组对象
```js
var people = [
  { name: 'Alice', age: 21 },
  { name: 'Max', age: 20 },
  { name: 'Jane', age: 20 }
];

function groupBy(objectArray, property) {
  return objectArray.reduce(function (acc, obj) {
    var key = obj[property];
    if (!acc[key]) {
      acc[key] = [];
    }
    acc[key].push(obj);
    return acc;
  }, {});
}

var groupedPeople = groupBy(people, 'age');
// groupedPeople is:
// { 
//   20: [
//     { name: 'Max', age: 20 }, 
//     { name: 'Jane', age: 20 }
//   ], 
//   21: [{ name: 'Alice', age: 21 }] 
// }
```

5. 应用场景：拼合数组
```js
var flattened = [[0, 1], [2, 3], [4, 5]].reduce(
  ( accumulator, currentValue ) => accumulator.concat(currentValue),
  []
);
// flattened is [0, 1, 2, 3, 4, 5]
```

6. 应用场景：使用 spread 运算符和 initialValue 拼合对象中数组
```js
var friends = [{
  name: 'Anna',
  books: ['Bible', 'Harry Potter'],
  age: 21
}, {
  name: 'Bob',
  books: ['War and peace', 'Romeo and Juliet'],
  age: 26
}, {
  name: 'Alice',
  books: ['The Lord of the Rings', 'The Shining'],
  age: 18
}];

// allbooks - list which will contain all friends' books +  
// additional list contained in initialValue
var allbooks = friends.reduce(function(accumulator, currentValue) {
  return [...accumulator, ...currentValue.books];
}, ['Alphabet']);

// allbooks = [
//   'Alphabet', 'Bible', 'Harry Potter', 'War and peace', 
//   'Romeo and Juliet', 'The Lord of the Rings',
//   'The Shining'
// ]
```

7. 删除数组中的重复项
```js
var myArray = ['a', 'b', 'a', 'b', 'c', 'e', 'e', 'c', 'd', 'd', 'd', 'd'];
var myOrderedArray = myArray.reduce(function (accumulator, currentValue) {
  if (accumulator.indexOf(currentValue) === -1) {
    accumulator.push(currentValue);
  }
  return accumulator
}, [])

console.log(myOrderedArray);
//['a', 'b', 'c', 'e', 'd']
```
- 注意：如果环境兼容 Set 和 Array.from() 可以如此实现
```js
let orderedArray = Array.from(new Set(myArray));
```

8. 按序列运行 Promise
```js
/**
 * Runs promises from array of functions that can return promises
 * in chained manner
 *
 * @param {array} arr - promise arr
 * @return {Object} promise object
 */
function runPromiseInSequence(arr, input) {
  return arr.reduce(
    (promiseChain, currentFunction) => promiseChain.then(currentFunction),
    Promise.resolve(input)
  );
}

// promise function 1
function p1(a) {
  return new Promise((resolve, reject) => {
    resolve(a * 5);
  });
}

// promise function 2
function p2(a) {
  return new Promise((resolve, reject) => {
    resolve(a * 2);
  });
}

// function 3  - will be wrapped in a resolved promise by .then()
function f3(a) {
 return a * 3;
}

// promise function 4
function p4(a) {
  return new Promise((resolve, reject) => {
    resolve(a * 4);
  });
}

const promiseArr = [p1, p2, f3, p4];
runPromiseInSequence(promiseArr, 10)
  .then(console.log);   // 1200
```

9. 功能块组合（enabling piping）
```js
// Building-blocks to use for composition
const double = x => x + x;
const triple = x => 3 * x;
const quadruple = x => 4 * x;

// Function composition enabling pipe functionality
const pipe = (...functions) => input => functions.reduce(
    (acc, fn) => fn(acc),
    input
);

// Composed functions for multiplication of specific values
const multiply6 = pipe(double, triple);
const multiply9 = pipe(triple, triple);
const multiply16 = pipe(quadruple, quadruple);
const multiply24 = pipe(double, triple, quadruple);

// Usage
multiply6(6); // 36
multiply9(9); // 81
multiply16(16); // 256
multiply24(10); // 240
```