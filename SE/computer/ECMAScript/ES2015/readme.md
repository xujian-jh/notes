# [ES2015] (ES6) Features

## Arrows and Lexical This

- Unlike functions, arrows share the same lexical this as their surrounding code.
- If an arrow is inside another function, it shares the "arguments" variable of its parent function.

```js
// no arrows
{
  ...
  addOptions: function (options) {
    var self = this;
    options.forEach(function(name, opts){
      self[name] = self.addChild(name, opts);
    });
  }
}

// arrows
{
  ...
  addOptions: function (options) {
    options.forEach((name, opts) => {
      this[name] = this.addChild(name, opts);
    });
  }
}
```

>no arrows：在过程函数中使用父级 `this`，需要将其显式缓存到另一个中间变量中，因为过程函数有独立的 `this` 变量，会覆盖父级。  
arrows：简写了过程函数，还省略掉了 `this` 的中间变量的定义。  
原因：arrows 没有独立的 `arguments`，所以其内部引用 `this` 对象会直接访问父级。

```js
// 完整写法
const getOptions = (name, key) => {
  ...
}

// 省略参数括号
const getOptions = key => {
  ...
}

// 省略参数和方法体括号
const getOptions = key => console.log(key);

// 无参数或方法体，括号不能省略
const noop = () => {};
```

## Classes

- Classes are a simple sugar over the prototype-based OO pattern.
- Classes support prototype-based inheritance, super calls, instance and static methods and constructors.

```js
class SkinnedMesh extends THREE.Mesh {
  constructor(geometry, materials) {
    super(geometry, materials);

    this.idMatrix = SkinnedMesh.defaultMatrix();
    this.bones = [];
    this.boneMatrices = [];
    //...
  }
  update(camera) {
    //...
    super.update();
  }
  static defaultMatrix() {
    return new THREE.Matrix4();
  }
}
```

## Enhanced Object Literals

- let object-based design benefit from some of the same conveniences.
  - setting the prototype at construction
  - shorthand
  - defining methods and making super calls

```js
var obj = {
    // Sets the prototype. "__proto__" or '__proto__' would also work.
    __proto__: theProtoObj,
    // Computed property name does not set prototype or trigger early error for duplicate __proto__ properties.
    ['__proto__']: somethingElse,

    // Shorthand for ‘handler: handler’
    handler,

    // Methods
    toString() {
     // Super calls
     return "d " + super.toString();
    }
};
```

## Template Strings

- Template strings provide syntactic sugar for constructing strings.

```js
// Basic literal string creation
`This is a pretty little template string.`

// Multiline strings
`In ES5 this is
 not legal.`

// Interpolate variable bindings
var name = "Bob", time = "today";
`Hello ${name}, how are you ${time}?`

// Unescaped template strings
String.raw`In ES5 "\n" is a line-feed.`

// Construct an HTTP request prefix is used to interpret the replacements and construction
GET`http://foo.org/bar?a=${a}&b=${b}
    Content-Type: application/json
    X-Credentials: ${credentials}
    { "foo": ${foo},
      "bar": ${bar}}`(myOnReadyStateChangeHandler);
```

## Destructuring

- Destructuring allows binding using pattern matching, with support for matching arrays and objects.
- Destructuring is fail-soft, similar to standard object lookup foo["bar"], producing undefined values when not found.

```js
// list matching
var [a, ,b] = [1,2,3];
a === 1;
b === 3;

// object matching
var { op: a, lhs: { op: b }, rhs: c }
       = getASTNode()

// object matching shorthand
// binds `op`, `lhs` and `rhs` in scope
var {op, lhs, rhs} = getASTNode()

// Can be used in parameter position
function g({name: x}) {
  console.log(x);
}
g({name: 5})

// Fail-soft destructuring
var [a] = [];
a === undefined;

// Fail-soft destructuring with defaults
var [a = 1] = [];
a === 1;

// Destructuring + defaults arguments
function r({x, y, w = 10, h = 10}) {
  return x + y + w + h;
}
r({x:1, y:2}) === 23
```

## Default + Rest + Spread

- Turn an array into consecutive `arguments` in a function call.

```js
function f(x, y=12) {
  // y is 12 if not passed (or passed as undefined)
  return x + y;
}
f(3) == 15
```

```js
function f(x, ...y) {
  // y is an Array
  return x * y.length;
}
f(3, "hello", true) == 6
```

```js
function f(x, y, z) {
  return x + y + z;
}
// Pass each elem of array as argument
f(...[1,2,3]) == 6
```

## Let + Const

- Block-scoped binding constructs.
  - `let` is the new var.
  - `const` is single-assignment.
- Static restrictions prevent use before assignment.

```js
function f() {
  {
    let x;
    {
      // this is ok since it's a block scoped name
      const x = "sneaky";
      // error, was just defined with `const` above
      x = "foo";
    }
    // this is ok since it was declared with `let`
    x = "bar";
    // error, already declared above in this block
    let x = "inner";
  }
}
```

## Iterators + For..Of

- Iterator objects enable custom iteration like CLR IEnumerable or Java Iterable.
- Don’t require realizing an array, enabling lazy design patterns like LINQ.

```js
let fibonacci = {
  [Symbol.iterator]() {
    let pre = 0, cur = 1;
    return {
      next() {
        [pre, cur] = [cur, pre + cur];
        return { done: false, value: cur }
      }
    }
  }
}

for (var n of fibonacci) {
  // truncate the sequence at 1000
  if (n > 1000)
    break;
  console.log(n);
}
```

## Generators

- Generators are subtypes of iterators which include additional `next` and `throw`.
  - These enable values to flow back into the generator.
- Generators simplify iterator-authoring using `function*` and `yield`.
  - `function*` returns a Generator instance.
  - `yield` is an expression form which returns a value (or throws).

```js
var fibonacci = {
  [Symbol.iterator]: function*() {
    var pre = 0, cur = 1;
    for (;;) {
      var temp = pre;
      pre = cur;
      cur += temp;
      yield cur;
    }
  }
}

for (var n of fibonacci) {
  // truncate the sequence at 1000
  if (n > 1000)
    break;
  console.log(n);
}
```

## Unicode

- Non-breaking additions to support full Unicode.
  - new RegExp u mode to handle code points.
  - new unicode literal form in strings.
  - new APIs to process strings at the 21bit code points level.

```js
// same as ES5.1
"𠮷".length == 2

// new RegExp behaviour, opt-in ‘u’
"𠮷".match(/./u)[0].length == 2

// new form
"\u{20BB7}" == "𠮷" == "\uD842\uDFB7"

// new String ops
"𠮷".codePointAt(0) == 0x20BB7

// for-of iterates code points
for(var c of "𠮷") {
  console.log(c);
}
```

## Modules

- Language-level support for modules for component definition.
  - Codifies patterns from popular JavaScript module loaders (AMD, CommonJS).
  - Runtime behaviour defined by a host-defined default loader.
  - Implicitly async model – no code executes until requested modules are available and processed.

```js
// lib/mathplusplus.js
export * from "lib/math";
export var e = 2.71828182846;
export default function(x) {
    return Math.exp(x);
}
```

```js
// app.js
import exp, {pi, e} from "lib/mathplusplus";
console.log("e^π = " + exp(pi));
```

## Map + Set + WeakMap + WeakSet

- WeakMaps provides leak-free object-key’d side tables.

```js
// Sets
var s = new Set();
s.add("hello").add("goodbye").add("hello");
s.size === 2;
s.has("hello") === true;

// Maps
var m = new Map();
m.set("hello", 42);
m.set(s, 34);
m.get(s) == 34;

// Weak Maps
var wm = new WeakMap();
wm.set(s, { extra: 42 });
wm.size === undefined

// Weak Sets
var ws = new WeakSet();
ws.add({ data: 42 });
// Because the added object has no other references, it will not be held in the set
```

---

[ES2015]:https://babeljs.io/docs/en/learn/