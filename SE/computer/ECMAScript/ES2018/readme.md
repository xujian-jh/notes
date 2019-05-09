# [What’s New in ES2018]

#### Asynchronous Iteration

- `async/await` keyword run asynchronous operations in series
  - `for … of` loops
  - `var` keyword is scoped to the nearest function block and `let` keyword is scoped to the nearest enclosing block, which can be smaller than a function block.
- `next();` method returns a Promise

```js
async function process(array) {
  for await (let i of array) {
    doSomething(i);
  }
  next();
}
```

#### Promise.finally()

- The `.finally()` prototype allows you to specify final logic in one place

```js
function doSomething() {
  doSomething1()
  .then(doSomething2)
  .then(doSomething3)
  .catch(err => {
    console.log(err);
  })
  .finally(() => {
    // finish here!
  });
}
```

#### The three-dot (...) notation

ES2015 introduced the rest parameters and spread operators. The three-dot (...) notation applied to array operations only.

ES2018 enables similar rest/spread functionality for object destructuring as well as arrays.

- Like arrays, you can only use a single rest parameter at the end of the declaration.
  -  In addition, it only works on the top level of each object and not sub-objects.

```js
restParam({
  a: 1,
  b: 2,
  c: 3
});

function restParam({ a, ...x }) {
  // a = 1
  // x = { b: 2, c: 3 }
}
```

- The spread operator can be used within other objects.
  - You only get shallow copies.
  - If a property holds another object, the clone will refer to the same object.
```js
const obj1 = { a: 1, b: 2, c: 3 };
const obj2 = { ...obj1, z: 26 };
// obj2 is { a: 1, b: 2, c: 3, z: 26 }
```

#### Regular Expression

1. Named Capture Groups

```js
const
  reDate = /([0-9]{4})-([0-9]{2})-([0-9]{2})/,
  match  = reDate.exec('2018-04-30'),
  year   = match[1], // 2018
  month  = match[2], // 04
  day    = match[3]; // 30
```

- ES2018 permits groups to be named using the notation `?<name>` immediately after the opening capture bracket `(`.
  - Named captures can also be used in `replace()` methods. 

```js
const
  reDate = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2})/,
  match  = reDate.exec('2018-04-30'),
  year   = match.groups.year,  // 2018
  month  = match.groups.month, // 04
  day    = match.groups.day;   // 30
```

```js
const
  reDate = /(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2})/,
  d      = '2018-04-30',
  usDate = d.replace(reDate, '$<month>-$<day>-$<year>');
```

2. Assertions

- lookahead assertions `(?=*)` inside a regular expression.

```js
const
  reLookahead = /\D(?=\d+)/,
  match       = reLookahead.exec('$123.89');

console.log( match[0] ); // $
```

- ES2018 introduces lookbehind assertions `(?<=*)` that work in the same way.
  - There’s also a negative lookbehind assertion `(?<!*)`, which sets that a value must not exist.

```js
const
  reLookbehind = /(?<=\D)\d+/,
  match        = reLookbehind.exec('$123.89');

console.log( match[0] ); // 123.89
```

```js
const
  reLookbehind = /(?<!\D)\d+/,
  match        = reLookbehind.exec('$123.89');

console.log( match[0] ); // null
```

3. ES2018 introduces `s` (dotAll) Flag

- A regular expression dot `.` matches any single character except line terminators.
```js
/^.$/.test('\n'); //false
```

- The `s` flag changes this behavior so line terminators are permitted. 

```js
/^.$/s.test('\n'); //true
```

4. ES2018 adds Unicode Property Escapes

- `/\p{*}/u`

```js
const reGreekSymbol = /\p{Script=Greek}/u;
reGreekSymbol.test('π'); // true
```

- `/\P{*}/u`

```js
const reGreekSymbol = /\P{Script=Greek}/u;
reGreekSymbol.test('π'); // false
```

#### [Template Literals Tweak]

1. Tagged templates function

```js
function foo(str) {
    return str[0].toUpperCase();
}

foo`justjavac`;
// 'JUSTJAVAC'
foo`Xyz`;
// 'XYZ'
```

2. `String.raw` is a built-in tagged templates function

```js
var str = String.raw`Hi\n${2+3}!`;
// 'Hi\\n5!'

str.length;
// 6

str.split('').join(',');
// 'H,i,\,n,5,!'
```

3. ES2018 revision of illegal escape sequences

- Illegal escape sequences will show up as `undefined` element in the “cooked” array.

```js
function latex(str) { 
 return { "cooked": str[0], "raw": str.raw[0] }
} 

latex`\unicode`

// { cooked: undefined, raw: "\\unicode" }
```

- Note that the escape sequence restriction is only dropped from tagged templates and not from untagged template literals.

```js
let bad = `bad escape sequence: \unicode`;
// SyntaxError: Invalid Unicode escape sequence
```

#

[What’s New in ES2018]:https://www.sitepoint.com/es2018-whats-new/

[Template Literals Tweak]:http://esnext.justjavac.com/proposal/template-literal-revision.html