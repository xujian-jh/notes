# [What’s New in ES2017]

## Async functions

- `async/await` make asynchronous calls even clearer.

```js
async function doSomething() {
  const
    response1 = await doSomething1(),
    response2 = await doSomething2(response1),
    response3 = await doSomething3(response2);
    next();
}
```

## Object

### Object.values()

- extract an array of values from name–value pairs within an object.

```js
const myObject = {
  a: 1,
  b: 'Two',
  c: [3,3,3]
}

const values = Object.values(myObject);
// [ 1, 'Two', [3,3,3] ]
```

### Object.entries()

- returns an array from an object containing name–value pairs.
- Each value in the returned array is a sub-array containing the name (index 0) and value (index 1).

```js
const myObject = {
  a: 1,
  b: 'Two',
  c: [3,3,3]
}

const entries = Object.entries(myObject);
/*
[
  [ 'a', 1 ],
  [ 'b', 'Two' ],
  [ 'c', [3,3,3] ]
]
*/
```

### Object.getOwnPropertyDescriptors()

- Returns another object containing all property descriptors (.value, .writable, .get, .set, .configurable, .enumerable).
- The properties are directly present on an object and not in the object’s prototype chain.
- `Object.getOwnPropertyDescriptor(object, property)` just one property descriptor.

```js
const myObject = {
  prop1: 'hello',
  prop2: 'world'
};

const descriptors = Object.getOwnPropertyDescriptors(myObject);

console.log(descriptors.prop1.writable); // true
console.log(descriptors.prop2.value);    // 'world'
```

## String Padding

- `.padStart()` and `.padEnd()`
- accept a minimum length
- an optional 'fill' string (space is the default) as parameters

```js
'abc'.padStart(5);         // '  abc'
'abc'.padStart(5,'-');     // '--abc'
'abc'.padStart(10, '123'); // '1231231abc'
'abc'.padStart(1);         // 'abc'

'abc'.padEnd(5);           // 'abc  '
'abc'.padEnd(5,'-');       // 'abc--'
'abc'.padEnd(10, '123');   // 'abc1231231'
'abc'.padEnd(1);           // 'abc'
```

## Trailing Commas are Permitted

1. object definitions
2. array declarations
3. function parameter lists

```js
const b = {
  a: 1,
  b: 2,
  c: 3,
};

const a = [1, 2, 3,];

function c(one,two,three,) {};
```

## SharedArrayBuffer and Atomics

- While both objects were implemented in Chrome and Firefox, it was disabled in January 2018 in response to the Spectre vulnerability.

---

[What’s New in ES2017]:https://www.sitepoint.com/es2017-whats-new/