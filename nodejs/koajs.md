阅读笔记：JavaScript 是单线程执行，同步容易阻塞，非阻塞唯有异步。B/S 结构 Server 端，推荐 [koajs 框架](https://koajs.com)（为避免“回调地狱”，使用 async 函数重写 expressjs 框架）。koajs 框架是基于 nodejs 实现 HTTP 封装（中间件 middleware）。

# 工程目录

1. 依赖描述文件 `package.json` 放入版本控制。
- 其中 `dependencies` 正确设置依赖项（包的版本号）。
- 其他字段均用来描述项目信息，可任意填写。
2. 依赖安装目录 `node_modules` 不放入版本控制。
- 在工程本目录下，执行 `npm install` 一次性安装依赖。
- 自动生成依赖安装目录 `node_modules`。

# 中间件 middleware

- 通过 `app.use()` 注册 async 函数为 middleware 。
- 参数 `ctx` 传入封装的 `request` 和 `response` 。
- 参数 `next` 传入将要处理的下一个 middleware 。
- `await next()` 实际调用下一个 middleware 。
- 多个 middleware 组成处理链，完成多个功能。

例如，3个 middleware 组成处理链，依次打印日志，记录处理时间，输出HTML：
```
// 导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');

// 创建一个Koa对象表示web app本身:
const app = new Koa();

// 对于任何请求，app将调用该异步函数处理请求：
app.use(async (ctx, next) => {
    console.log(`${ctx.request.method} ${ctx.request.url}`); // 打印URL
    await next(); // 调用下一个middleware
});

app.use(async (ctx, next) => {
    const start = new Date().getTime(); // 当前时间
    await next(); // 调用下一个middleware
    const ms = new Date().getTime() - start; // 耗费时间
    console.log(`Time: ${ms}ms`); // 打印耗费时间
});

app.use(async (ctx, next) => {
    await next();
    ctx.response.type = 'text/html';
    ctx.response.body = '<h1>Hello, koa2!</h1>';
});

// 在端口3000监听:
app.listen(3000);
console.log('app started at port 3000...');
```
- middleware 的顺序很重要，如果一个 middleware 没有调用 `await next()`，后续的 middleware 将不再执行。

例如，检测用户权限的 middleware 决定是否继续处理请求，还是直接返回403错误：
```
app.use(async (ctx, next) => {
    if (await checkUserPermission(ctx)) {
        await next();
    } else {
        ctx.response.status = 403;
    }
});
```
- 简写 `ctx.url` 相当于 `ctx.request.url`。
- 简写 `ctx.type` 相当于 `ctx.response.type`。

# koa-router（处理 URL 映射的 middleware）

1. `package.json` 中添加依赖项：
```
"koa-router": "7.0.0"
```
2. 命令 `npm install` 安装依赖。
3. 使用 `koa-router` 来处理 `URL`：
```
const Koa = require('koa');

// 注意require('koa-router')返回的是函数:
const router = require('koa-router')();

const app = new Koa();

// log request URL:
app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
});

// add url-route:
router.get('/hello/:name', async (ctx, next) => {
    var name = ctx.params.name;
    ctx.response.body = `<h1>Hello, ${name}!</h1>`;
});

router.get('/', async (ctx, next) => {
    ctx.response.body = '<h1>Index</h1>';
});

// add router middleware:
app.use(router.routes());

app.listen(3000);
console.log('app started at port 3000...');
```

# `koa-bodyparser`（解析 `request body` 的 middleware）

1. `package.json` 中添加依赖项：
```
"koa-bodyparser": "3.2.0"
```
2. 命令 `npm install` 安装依赖。
3. `koa-bodyparser` 必须在 `router` 之前被注册到app对象上。
```
const Koa = require('koa');

const bodyParser = require('koa-bodyparser');

const router = require('koa-router')();

const app = new Koa();

// log request URL:
app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
});

// parse request body:
app.use(bodyParser());

// add url-route:
router.get('/hello/:name', async (ctx, next) => {
    var name = ctx.params.name;
    ctx.response.body = `<h1>Hello, ${name}!</h1>`;
});

router.get('/', async (ctx, next) => {
    ctx.response.body = `<h1>Index</h1>
        <form action="/signin" method="post">
            <p>Name: <input name="name" value="koa"></p>
            <p>Password: <input name="password" type="password"></p>
            <p><input type="submit" value="Submit"></p>
        </form>`;
});

router.post('/signin', async (ctx, next) => {
    var
        name = ctx.request.body.name || '',
        password = ctx.request.body.password || '';
    console.log(`signin with name: ${name}, password: ${password}`);
    if (name === 'koa' && password === '12345') {
        ctx.response.body = `<h1>Welcome, ${name}!</h1>`;
    } else {
        ctx.response.body = `<h1>Login failed!</h1>
        <p><a href="/">Try again</a></p>`;
    }
});

// add router middleware:
app.use(router.routes());

app.listen(3000);
console.log('app started at port 3000...');
```

# 模块化集中 URL 映射（代码分离，逻辑清晰）

1. 所有处理 URL 的函数按功能组存放在 controllers 目录
- 在 controllers 目录下编写 `index.js` ：
```
var fn_index = async (ctx, next) => {
    ctx.response.body = `<h1>Index</h1>
        <form action="/signin" method="post">
            <p>Name: <input name="name" value="koa"></p>
            <p>Password: <input name="password" type="password"></p>
            <p><input type="submit" value="Submit"></p>
        </form>`;
};

var fn_signin = async (ctx, next) => {
    var
        name = ctx.request.body.name || '',
        password = ctx.request.body.password || '';
    console.log(`signin with name: ${name}, password: ${password}`);
    if (name === 'koa' && password === '12345') {
        ctx.response.body = `<h1>Welcome, ${name}!</h1>`;
    } else {
        ctx.response.body = `<h1>Login failed!</h1>
        <p><a href="/">Try again</a></p>`;
    }
};

module.exports = {
    'GET /': fn_index,
    'POST /signin': fn_signin
};
```
这个 `index.js` 通过 `module.exports` 把两个 URL 处理函数暴露出来。

- 类似的 `hello.js` 把一个 URL 处理函数暴露出来：
```
var fn_hello = async (ctx, next) => {
    var name = ctx.params.name;
    ctx.response.body = `<h1>Hello, ${name}!</h1>`;
};

module.exports = {
    'GET /hello/:name': fn_hello
};
```
2. `controller.js`（扫描目录默认为 controllers 和创建 router 的 middleware）
```

const fs = require('fs');

// add url-route in /controllers:

function addMapping(router, mapping) {
    for (var url in mapping) {
        if (url.startsWith('GET ')) {
            var path = url.substring(4);
            router.get(path, mapping[url]);
            console.log(`register URL mapping: GET ${path}`);
        } else if (url.startsWith('POST ')) {
            var path = url.substring(5);
            router.post(path, mapping[url]);
            console.log(`register URL mapping: POST ${path}`);
        } else if (url.startsWith('PUT ')) {
            var path = url.substring(4);
            router.put(path, mapping[url]);
            console.log(`register URL mapping: PUT ${path}`);
        } else if (url.startsWith('DELETE ')) {
            var path = url.substring(7);
            router.del(path, mapping[url]);
            console.log(`register URL mapping: DELETE ${path}`);
        } else {
            console.log(`invalid URL: ${url}`);
        }
    }
}

function addControllers(router, dir) {
    fs.readdirSync(__dirname + '/' + dir).filter((f) => {
        return f.endsWith('.js');
    }).forEach((f) => {
        console.log(`process controller: ${f}...`);
        let mapping = require(__dirname + '/' + dir + '/' + f);
        addMapping(router, mapping);
    });
}

module.exports = function (dir) {
    let
        // 如果不传参数，扫描目录默认为'controllers'
        controllers_dir = dir || 'controllers',
        router = require('koa-router')();
    addControllers(router, controllers_dir);
    return router.routes();
};
```
3. 在 `app.js` 的代码简化为：
```
...

// 导入controller middleware:
const controller = require('./controller');

...

// 使用middleware:
app.use(controller());

...
```