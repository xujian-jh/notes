阅读笔记：koajs 框架精华是 [use async functions as  middleware](https://github.com/koajs/koa/blob/master/docs/guide.md) 。为了兼容旧版本，koajs 框架仍然保留 `commonFunction` 或 `generatorFunction` 。

# 中间件（Middleware）

- 中间件：异步返回函数 `async function MiddlewareFunction（ctx，next）`。
- 函数内 `await next()` 手动调用 "下一个（downstream）" 中间件。

例如，通过添加 `X-Response-Time` 标头字段来跟踪请求通过Koa传播所需的时间。
```
async function responseTime(ctx, next) {
  const start = Date.now();
  await next();
  const ms = Date.now() - start;
  ctx.set('X-Response-Time', `${ms}ms`);
}

app.use(responseTime);
```

- 多个中间件组成一条处理链；如果某个中间件缺省 `await next()` 处理链就断裂，后续中间件不执行。
- `await next()` 之前，可以视为“捕获”阶段。
- `await next()` 之后，可以视为“冒泡”阶段。

动画示意：中间件的堆栈流（链的实现）
![middleware.gif](./middleware.gif)
1. 创建日期以跟踪响应时间
2. 等待控制下一个中间件
3. 创建另一个日期来跟踪持续时间
4. 等待控制下一个中间件
5. 将响应主体设置为“Hello World”
6. 计算持续时间
7. 输出日志行
8. 计算响应时间
9. 设置X-Response-Time标题字段
10. 交给Koa处理响应

# 中间件最佳实践（Middleware Best Practices）

1. 中间件选项  
惯例：创建公共中间件时，接受选项允许用户扩展。
```
function logger(format) {
  format = format || ':method ":url"';

  return async function (ctx, next) {
    const str = format
      .replace(':method', ctx.method)
      .replace(':url', ctx.url);

    console.log(str);

    await next();
  };
}

app.use(logger());
app.use(logger(':method :url'));
```
实践：中间件命名，为调试目的分配名称很有用。
```
function  logger（format）{
   return  async  function  logger（ctx，next）{ 

  }; 
}
```
2. 中间件 `koa-compose` 将多个中间件“组合”成一个中间件。
```
const compose = require('koa-compose');

async function random(ctx, next) {
  if ('/random' == ctx.path) {
    ctx.body = Math.floor(Math.random() * 10);
  } else {
    await next();
  }
};

async function backwards(ctx, next) {
  if ('/backwards' == ctx.path) {
    ctx.body = 'sdrawkcab';
  } else {
    await next();
  }
}

async function pi(ctx, next) {
  if ('/pi' == ctx.path) {
    ctx.body = String(Math.PI);
  } else {
    await next();
  }
}

const all = compose([random, backwards, pi]);

app.use(all);
```
3. 中间件异步操作  
异步函数和承诺构成了Koa的基础，允许您编写非阻塞顺序代码。  
例如，中间件读取文件名 `./docs.md` 的内容。
```
const fs = require('fs-promise');

app.use(async function (ctx, next) {
  const paths = await fs.readdir('docs');
  const files = await Promise.all(paths.map(path => fs.readFile(`docs/${path}`, 'utf8')));

  ctx.type = 'markdown';
  ctx.body = files.join('');
});
```
4. 调试Koa（Debugging Koa）  
- `DEBUG=koa*` 查看 DEBUG 环境变量，看所使用的中间件列表。
```
$ DEBUG=koa* node --harmony examples/simple
  koa:application use responseTime +0ms
  koa:application use logger +4ms
  koa:application use contentLength +0ms
  koa:application use notfound +0ms
  koa:application use response +0ms
  koa:application listen +0ms
```
- `._name` 设置中间件的名称。
```
const path = require('path');
const serve = require('koa-static');

const publicFiles = serve(path.join(__dirname, 'public'));
publicFiles._name = 'static /public';

app.use(publicFiles);

//  查看 DEBUG 环境变量
//  koa:application use static /public +0ms
```