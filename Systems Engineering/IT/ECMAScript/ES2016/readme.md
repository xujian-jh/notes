# What’s New in ES2016

## Array.prototype.includes(value : any) : boolean

- The array `.includes()` method, which returns `true` or `false` when a value is contained in an array.

```js
assert([1, 2, 3].includes(2) === true);
assert([1, 2, 3].includes(4) === false);

assert([1, 2, NaN].includes(NaN) === true);

assert([1, 2, -0].includes(+0) === true);
assert([1, 2, +0].includes(-0) === true);

assert(["a", "b", "c"].includes("a") === true);
assert(["a", "b", "c"].includes("a", 1) === false);
```

## Exponentiation operator (`**`)

- The `a ** b` exponentiation operator, which is identical to `Math.pow(a, b)`

```js
2**2*2 //8
2**(2*2) //16
```