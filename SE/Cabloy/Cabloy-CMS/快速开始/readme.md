# 新建Cabloy项目

## 初始化项目目录

```s
$ npm init cabloy cabloy-cms --type=cabloy
$ cd cabloy-cms
$ tree -a              # 树形结构详细查看
.
├── .babelrc
├── build
│   └── config.js
├── .editorconfig
├── .eslintignore
├── .eslintrc.js
├── .gitignore
├── nginx-cms.conf
├── nginx.conf
├── package.json
├── README.md
└── src
    ├── backend
    │   ├── config
    │   │   ├── config.default.js
    │   │   ├── config.local.js
    │   │   ├── config.prod.js
    │   │   ├── config.unittest.js
    │   │   └── locale
    │   │       └── zh-cn.js
    │   └── package.json
    ├── front
    │   ├── assets
    │   │   └── css
    │   │       ├── app.less
    │   │       └── module
    │   │           └── .gitkeep
    │   ├── config
    │   │   ├── config.js
    │   │   ├── locale
    │   │   │   └── zh-cn.js
    │   │   └── locales.js
    │   └── main.js
    └── module
        └── test-party
            ├── .babelrc
            ├── backend
            │   ├── src
            │   │   ├── config
            │   │   │   ├── config.js
            │   │   │   ├── errors.js
            │   │   │   ├── locale
            │   │   │   │   └── zh-cn.js
            │   │   │   ├── locales.js
            │   │   │   ├── middlewares.js
            │   │   │   └── validation
            │   │   │       └── schemas.js
            │   │   ├── controller
            │   │   │   ├── party.js
            │   │   │   ├── partyPublic.js
            │   │   │   ├── test
            │   │   │   │   ├── atom
            │   │   │   │   │   ├── all.js
            │   │   │   │   │   ├── publicFlow.js
            │   │   │   │   │   ├── right.js
            │   │   │   │   │   └── starLabel.js
            │   │   │   │   ├── ctx
            │   │   │   │   │   ├── performAction.js
            │   │   │   │   │   ├── session.js
            │   │   │   │   │   ├── tail.js
            │   │   │   │   │   └── transaction.js
            │   │   │   │   ├── event
            │   │   │   │   │   └── userVerify.js
            │   │   │   │   ├── feat
            │   │   │   │   │   ├── httpLog.js
            │   │   │   │   │   ├── sendMail.js
            │   │   │   │   │   └── startup.js
            │   │   │   │   ├── function
            │   │   │   │   │   ├── all.js
            │   │   │   │   │   ├── public.js
            │   │   │   │   │   └── right.js
            │   │   │   │   └── role
            │   │   │   │       └── userRole.js
            │   │   │   └── version.js
            │   │   ├── main.js
            │   │   ├── meta.js
            │   │   ├── model
            │   │   │   ├── party.js
            │   │   │   ├── partyPublic.js
            │   │   │   └── partyType.js
            │   │   ├── models.js
            │   │   ├── routes.js
            │   │   ├── service
            │   │   │   ├── party.js
            │   │   │   ├── partyPublic.js
            │   │   │   ├── version
            │   │   │   │   ├── testData.js
            │   │   │   │   └── test.js
            │   │   │   └── version.js
            │   │   └── services.js
            │   └── test
            │       └── controller
            │           └── test
            │               ├── atom
            │               │   ├── all.test.js
            │               │   ├── publicFlow.test.js
            │               │   ├── right.test.js
            │               │   └── starLabel.test.js
            │               ├── auth
            │               │   ├── echo.test.js
            │               │   └── login.test.js
            │               ├── ctx
            │               │   ├── performAction.test.js
            │               │   ├── session.test.js
            │               │   ├── tail.test.js
            │               │   └── transaction.test.js
            │               ├── feat
            │               │   ├── httpLog.test.js
            │               │   └── sendMail.test.js
            │               ├── function
            │               │   ├── all.test.js
            │               │   ├── public.test.js
            │               │   └── right.test.js
            │               └── role
            │                   └── userRole.test.js
            ├── build
            │   ├── backend
            │   │   ├── build.js
            │   │   ├── config.js
            │   │   ├── webpack.base.conf.js
            │   │   └── webpack.prod.conf.js
            │   ├── config.js
            │   └── front
            │       ├── build.js
            │       ├── config.js
            │       ├── utils.js
            │       ├── webpack.base.conf.js
            │       └── webpack.prod.conf.js
            ├── .editorconfig
            ├── .eslintignore
            ├── .eslintrc.js
            ├── front
            │   └── src
            │       ├── assets
            │       │   └── css
            │       │       └── module.css
            │       ├── components.js
            │       ├── config
            │       │   ├── config.js
            │       │   ├── locale
            │       │   │   └── zh-cn.js
            │       │   └── locales.js
            │       ├── main.js
            │       ├── pages
            │       │   └── test
            │       │       └── select.vue
            │       ├── routes.js
            │       └── store.js
            ├── package.json
            └── README.md

49 directories, 101 files
```

- 项目名称 cabloy-cms
  - 150 项 = 49 directories, 91 files（10 files 隐藏）
  - 共 277.7 kB

## 项目 cabloy-cms 依据 package.json 安装 Cabloy 模板及依赖

```s
npm i
```

- 项目模板 node_modules
  - 42,294 项，共 252.2 MB

## 项目 cabloy-cms 直接安装 CMS 模块及依赖

```s
npm i egg-born-module-a-cms
```

- 项目模板 node_modules
  - 42,488 项，共 253.1 MB

## 项目 cabloy-cms 直接安装 CMS 博客主题模块及依赖

```s
npm i egg-born-module-cms-themeblog
```

- 项目模板 node_modules
  - 43,379 项，共 258.2 MB

## 运行

### 启动后端服务

```s
npm run dev:backend
```

### 启动前端服务

```s
npm run dev:front
```
