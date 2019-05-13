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

[ES2015]:https://babeljs.io/docs/en/learn/