阅读笔记：Client/Server模式简称CS架构，Browser/Server模式简称BS架构。javascript事实上统治着Browser端，nodejs把javascript引入Server端。

# nodejs

- 从[nodejs官网](https://nodejs.org/en/)下载对应平台的安装程序。
- 在Windows上安装时务必选择全部组件，包括勾选Add to Path。
- 命令行 `node -v` 查看nodejs版本。
- 在命令行模式直接运行javascript文件（`.js`），想要输出结果必须自己用 `console.log()` 打印出来。  
- 在命令行模式传递 `--use_strict` 参数来开启严格模式。
- 命令行 `node` 进入nodejs交互模式。  
- 看到 `>` 是在nodejs交互模式（会把每一行javascript代码的结果自动打印出来）。  
- 退出nodejs交互模式，连按两次Ctrl+C。
- 在编写javascript代码的时候，完全可以一边在文本编辑器里写代码，一边开一个nodejs交互模式窗口，在写代码的过程中，把部分代码粘到nodejs交互模式去验证，事半功倍！前提是得有个27'的超大显示器！

# npm（nodejs package manager）

- npm是javascript的包管理器和世界上最大的软件注册表。采用包方式管理可重用的代码。
- npm可以根据依赖关系，把所有依赖的包都下载下来并管理起来。
- npm已经在nodejs安装的时候顺带装好。
- 命令行 `npm -v` 查看npm版本。

# 模块（module）

- 提高了代码的可维护性。函数分组放到不同的文件，每个文件包含的代码就相对较少。
- 提高了代码的可重用性。当一个模块编写完毕可以被其他地方引用。经常引用其他模块，包括nodejs内置的模块和来自第三方的模块。
- 每个.js文件都是一个模块，可以避免函数名和变量名冲突。
- 模块加载机制被称为CommonJS规范。实现“模块”功能的奥妙就在于javascript是一种函数式编程语言，它支持闭包。如果我们把一段javascript代码用一个函数包装起来，这段代码的所有“全局”变量就变成了函数内部的局部变量，所以需要最后对外暴露变量。
- 模块想要对外暴露变量（函数也是变量），用 `module.exports = variable` 。
- 引用模块暴露的变量，用 `var ref = require('module_name')` 。
```
// 准备module对象:
var module = {
    id: 'hello',
    exports: {}
};
var load = function (module) {
    // 读取的hello.js代码:
    function greet(name) {
        console.log('Hello, ' + name + '!');
    }

    module.exports = greet;
    // hello.js代码结束
    return module.exports;
};
var exported = load(module);
// 保存module:
save(module, exported);
```
Node实现javascript模块的原理介绍：
1. 变量module是Node在加载js文件前准备的一个变量，并将其传入加载函数，我们在hello.js中可以直接使用变量module原因就在于它实际上是函数的一个参数：`module.exports = greet;`
通过把参数module传递给load()函数，hello.js就顺利地把一个变量传递给了Node执行环境，Node会把module变量保存到某个地方。
2. 由于Node保存了所有导入的module，当我们用require()获取module时，Node找到对应的module，把这个module的exports变量返回，这样，另一个模块就顺利拿到了模块的输出：`var greet = require('./hello');`  

# fs模块

Node.js内置的fs模块就是文件系统模块，负责读写文件。
- 按照JavaScript的标准，异步读取一个文本文件时，回调函数的data参数将返回一个String对象。
```
'use strict';

var fs = require('fs');

fs.readFile('sample.txt', 'utf-8', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
```
- 当异步读取二进制文件时，回调函数的data参数将返回一个Buffer对象。在Node.js中，Buffer对象就是一个包含零个或任意个字节的数组（注意和Array不同）。
```
'use strict';

var fs = require('fs');

fs.readFile('sample.png', function (err, data) {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
        console.log(data.length + ' bytes');
    }
});
```
Buffer对象可以和String对象相互转换：
```
// Buffer -> String
var text = data.toString('utf-8');
console.log(text);
```
```
// String -> Buffer
var buf = Buffer.from(text, 'utf-8');
console.log(buf);
```

# stream模块

stream是Node.js提供的一个仅在服务区端可用的模块，目的是支持“流”这种数据结构。
- 从键盘输入到应用程序，实际上它还对应着一个名字：标准输入流（stdin）。
- 如果应用程序把字符一个一个输出到显示器上，这也可以看成是一个流，这个流也有名字：标准输出流（stdout）。
- 流是一种抽象的数据结构。
- 流的特点是数据是有序的，而且必须依次读取，或者依次写入，不能像Array那样随机定位。
- 在Node.js中，流也是一个对象，我们只需要响应流的事件就可以了：  
`data`事件表示流的数据已经可以读取了;  
`end`事件表示这个流已经到末尾了，没有数据可以读取了;  
`error`事件表示出错了。

一个从文件流读取文本内容要注意，`data`事件可能会有多次，每次传递的`chunk`是流的一部分数据。：
```
'use strict';

var fs = require('fs');

// 打开一个流:
var rs = fs.createReadStream('sample.txt', 'utf-8');

rs.on('data', function (chunk) {
    console.log('DATA:')
    console.log(chunk);
});

rs.on('end', function () {
    console.log('END');
});

rs.on('error', function (err) {
    console.log('ERROR: ' + err);
});
```
以流的形式写入文件，只需要不断调用 `write()` 方法，最后以 `end()` 结束：
```
'use strict';

var fs = require('fs');

var ws1 = fs.createWriteStream('output1.txt', 'utf-8');
ws1.write('使用Stream写入文本数据...\n');
ws1.write('END.');
ws1.end();

var ws2 = fs.createWriteStream('output2.txt');
ws2.write(new Buffer('使用Stream写入二进制数据...\n', 'utf-8'));
ws2.write(new Buffer('END.', 'utf-8'));
ws2.end();
```
- 所有可以读取数据的流都继承自stream.Readable，所有可以写入的流都继承自stream.Writable。
- 所有的数据自动从Readable流进入Writable流，这种操作叫pipe。

在Node.js中，Readable流有一个pipe()方法，就是用来干这件事的。这实际上是一个复制文件的程序：
```
'use strict';

var fs = require('fs');

var rs = fs.createReadStream('sample.txt');
var ws = fs.createWriteStream('copied.txt');

rs.pipe(ws);
```
默认情况下，当Readable流的数据读取完毕，end事件触发后，将自动关闭Writable流。如果我们不希望自动关闭Writable流，需要传入参数：
```
readable.pipe(writable, { end: false });
```

# http模块

Node.js自带的http模块解析HTTP协议，提供的request对象封装了HTTP请求，response对象封装了HTTP响应。  
- HTTP服务器  
用Node.js实现一个HTTP服务器程序非常简单。我们来实现一个最简单的Web程序hello.js，它对于所有请求，都返回Hello world!：
```
'use strict';

// 导入http模块:
var http = require('http');

// 创建http server，并传入回调函数:
var server = http.createServer(function (request, response) {
    // 回调函数接收request和response对象,
    // 获得HTTP请求的method和url:
    console.log(request.method + ': ' + request.url);
    // 将HTTP响应200写入response, 同时设置Content-Type: text/html:
    response.writeHead(200, {'Content-Type': 'text/html'});
    // 将HTTP响应的HTML内容写入response:
    response.end('<h1>Hello world!</h1>');
});

// 让服务器监听8080端口:
server.listen(8080);

console.log('Server is running at http://127.0.0.1:8080/');

// in command-line
// $ node hello.js 
// Server is running at http://127.0.0.1:8080/
//
// in browser
// http://localhost:8080/
```
- HTTP文件服务器  
可以设定一个目录，然后让Web程序变成一个文件服务器。要实现这一点，我们只需要解析 `request.url` 中的路径，然后在本地找到对应的文件，把文件内容发送出去就可以了。
```
'use strict';

var fs = require('fs'),
    url = require('url'),
    path = require('path'),
    http = require('http');

// 从命令行参数获取root目录，默认是当前目录
var root = path.resolve(process.argv[2] || '.');
console.log('Static root directory: ' + root);

// 创建服务器
var server = http.createServer(function(request, response){
    // 获得URL的path，类似 /css/bootstrap.css
    var pathname = url.parse(request.url).pathname;
    // 获得对应的本地文件路径，类似 /srv/www/css/bootstrap.css
    var filepath = path.join(root, pathname);
    // 获取文件状态
    // 如果HTTP请求的是目录，则自动在此路径下依次搜索index.html和default.html，
    // 若找到，就返回HTML文件的内容
    var defaultPages = ['/index.html', '/default.html'];

    var pageCount = 0;

    function getDefaultPage(){
        if(pageCount === defaultPages.length){
            get404Page();
            return;
        }
        var page = path.join(filepath, defaultPages[pageCount]);
        fs.stat(page, function(err, stats){
            if(err || !stats.isFile()){
                pageCount++;
                getDefaultPage();
            }else{
                get200Page(page);
            }
        });
    };

    function get404Page(){
        // 出错或者文件不存在
        console.log('404 ' + request.url);
        // 发送404响应
        response.writeHead(404);
        response.end('404 Not Found');
    };

    function get200Page(filepath){
        console.log('200 ' + request.url);
        response.writeHead(200);
        fs.createReadStream(filepath).pipe(response);
    }

    fs.stat(filepath, function(err, stats){
        if(err){
            get404Page();
        }else if(stats.isFile()){
            get200Page(filepath);
        }else if(stats.isDirectory()){
            getDefaultPage();
        }
    });
}); 

server.listen(8989);
console.log('Server is running at http://127.0.0.1:8989/');

// in command-line
// $ node file_server.js /path/to/dir
// Static root directory: /path/to/dir
// Server is running at http://127.0.0.1:8989/
//
// in browser
// http://localhost:8989/
```
只要当前目录下存在文件index.html或default.html，服务器就可以把文件内容发送给浏览器。观察控制台输出：
```
200 /index.html
200 /css/uikit.min.css
200 /js/jquery.min.js
200 /fonts/fontawesome-webfont.woff2
```
第一个请求是浏览器请求index.html页面，后续请求是浏览器解析HTML后发送的其它资源请求。

# url模块

解析URL需要用到Node.js提供的url模块，它使用起来非常简单，通过parse()将一个字符串解析为一个Url对象：
```
'use strict';

var url = require('url');

console.log(url.parse('http://user:pass@host.com:8080/path/to/file?query=string#hash'));
```
结果如下：
```
Url {
  protocol: 'http:',
  slashes: true,
  auth: 'user:pass',
  host: 'host.com:8080',
  port: '8080',
  hostname: 'host.com',
  hash: '#hash',
  search: '?query=string',
  query: 'query=string',
  pathname: '/path/to/file',
  path: '/path/to/file?query=string',
  href: 'http://user:pass@host.com:8080/path/to/file?query=string#hash' }
```

# path模块

处理本地文件目录需要使用Node.js提供的path模块，它可以方便地构造目录：
```
'use strict';

var path = require('path');

// 解析当前目录:
var workDir = path.resolve('.'); // '/Users/michael'

// 组合完整的文件路径:当前目录+'pub'+'index.html':
var filePath = path.join(workDir, 'pub', 'index.html');
// '/Users/michael/pub/index.html'
```
使用path模块可以正确处理操作系统相关的文件路径。在Windows系统下，返回的路径类似于C:\Users\michael\static\index.html，这样，我们就不关心怎么拼接路径了。

# crypto模块

crypto模块的目的是为了提供通用的加密算法。用纯JavaScript代码实现这些功能不是不可能，但速度会非常慢。Nodejs用C/C++实现这些算法后，通过cypto模块暴露为JavaScript接口，使用方便，运行速度也快。
- MD5、SHA1、sha256和sha512  
MD5是一种常用的哈希算法，用于给任意数据一个“签名”。这个签名通常用一个十六进制的字符串表示：
```
const crypto = require('crypto');

const hash = crypto.createHash('md5');

// 可任意多次调用update():
hash.update('Hello, world!');
hash.update('Hello, nodejs!');

console.log(hash.digest('hex')); // 7e1977739c748beac0c0fd14fd26a544
```
update()方法默认字符串编码为UTF-8，也可以传入Buffer。  
如果要计算SHA1，只需要把'md5'改成'sha1'，就可以得到SHA1的结果1f32b9c9932c02227819a4151feed43e131aca40。  
还可以使用更安全的sha256和sha512。
- Hmac  
Hmac算法是一种“增强”的哈希算法，利用MD5或SHA1等哈希算法，还需要一个密钥：
```
const crypto = require('crypto');

const hmac = crypto.createHmac('sha256', 'secret-key');

hmac.update('Hello, world!');
hmac.update('Hello, nodejs!');

console.log(hmac.digest('hex')); // 80f7e22570...
```
只要密钥发生了变化，那么同样的输入数据也会得到不同的签名。
- AES  
AES是一种常用的对称加密算法，加解密都用同一个密钥。crypto模块提供了AES支持，但是需要自己封装好函数，便于使用：
```
const crypto = require('crypto');

function aesEncrypt(data, key) {
    const cipher = crypto.createCipher('aes192', key);
    var crypted = cipher.update(data, 'utf8', 'hex');
    crypted += cipher.final('hex');
    return crypted;
}

function aesDecrypt(encrypted, key) {
    const decipher = crypto.createDecipher('aes192', key);
    var decrypted = decipher.update(encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
}

var data = 'Hello, this is a secret message!';
var key = 'Password!';
var encrypted = aesEncrypt(data, key);
var decrypted = aesDecrypt(encrypted, key);

console.log('Plain text: ' + data);
console.log('Encrypted text: ' + encrypted);
console.log('Decrypted text: ' + decrypted);

\\ 运行结果如下：
\\ Plain text: Hello, this is a secret message!
\\ Encrypted text: 8a944d97bdabc157a5b7a40cb180e7...
\\ Decrypted text: Hello, this is a secret message!
```
- Diffie-Hellman  
DH算法是一种密钥交换协议，它可以让双方在不泄漏密钥的情况下协商出一个密钥来。DH算法基于数学原理，比如小明和小红想要协商一个密钥，可以这么做：

1. 小明先选一个素数和一个底数，例如，素数p=23，底数g=5（底数可以任选），再选择一个秘密整数a=6，计算A=g^a mod p=8，然后大声告诉小红：p=23，g=5，A=8；

2. 小红收到小明发来的p，g，A后，也选一个秘密整数b=15，然后计算B=g^b mod p=19，并大声告诉小明：B=19；

3. 小明自己计算出s=B^a mod p=2，小红也自己计算出s=A^b mod p=2，因此，最终协商的密钥s为2。

4. 在这个过程中，密钥2并不是小明告诉小红的，也不是小红告诉小明的，而是双方协商计算出来的。第三方只能知道p=23，g=5，A=8，B=19，由于不知道双方选的秘密整数a=6和b=15，因此无法计算出密钥2。

用crypto模块实现DH算法如下：
```
const crypto = require('crypto');

// xiaoming's keys:
var ming = crypto.createDiffieHellman(512);
var ming_keys = ming.generateKeys();

var prime = ming.getPrime();
var generator = ming.getGenerator();

console.log('Prime: ' + prime.toString('hex'));
console.log('Generator: ' + generator.toString('hex'));

// xiaohong's keys:
var hong = crypto.createDiffieHellman(prime, generator);
var hong_keys = hong.generateKeys();

// exchange and generate secret:
var ming_secret = ming.computeSecret(hong_keys);
var hong_secret = hong.computeSecret(ming_keys);

// print secret:
console.log('Secret of Xiao Ming: ' + ming_secret.toString('hex'));
console.log('Secret of Xiao Hong: ' + hong_secret.toString('hex'));

// 运行后，可以得到如下输出：
// $ node dh.js 
// Prime: a8224c...deead3
// Generator: 02
// Secret of Xiao Ming: 695308...d519be
// Secret of Xiao Hong: 695308...d519be
// 注意每次输出都不一样，因为素数的选择是随机的。
```
- RSA  
RSA算法是一种非对称加密算法，即由一个私钥和一个公钥构成的密钥对，通过私钥加密，公钥解密，或者通过公钥加密，私钥解密。其中，公钥可以公开，私钥必须保密。  
1. 在使用Node进行RSA加密前，命令行生成一个RSA密钥对：
```
openssl genrsa -aes256 -out rsa-key.pem 2048
```
根据提示输入密码，这个密码是用来加密RSA密钥的，加密方式指定为AES256，生成的RSA的密钥长度是2048位。执行成功后，我们获得了加密的rsa-key.pem文件。

2. 通过上面的rsa-key.pem加密文件，我们可以导出原始的私钥，命令如下：  
```
openssl rsa -in rsa-key.pem -outform PEM -out rsa-prv.pem
```
输入第一步的密码，我们获得了解密后的私钥。

3. 类似的，我们用下面的命令导出原始的公钥：
```
openssl rsa -in rsa-key.pem -outform PEM -pubout -out rsa-pub.pem
```
这样，我们就准备好了原始私钥文件 `rsa-prv.pem` 和原始公钥文件 `rsa-pub.pem` ，编码格式均为PEM。

使用crypto模块提供的方法，即可实现非对称加解密:
```
const
    fs = require('fs'),
    crypto = require('crypto');

// 从文件加载key:
function loadKey(file) {
    // key实际上就是PEM编码的字符串:
    return fs.readFileSync(file, 'utf8');
}

let
    prvKey = loadKey('./rsa-prv.pem'),
    pubKey = loadKey('./rsa-pub.pem'),
    message = 'Hello, world!';

// 使用私钥加密:
let enc_by_prv = crypto.privateEncrypt(prvKey, Buffer.from(message, 'utf8'));
console.log('encrypted by private key: ' + enc_by_prv.toString('hex'));


let dec_by_pub = crypto.publicDecrypt(pubKey, enc_by_prv);
console.log('decrypted by public key: ' + dec_by_pub.toString('utf8'));
```
执行后，可以得到解密后的消息，与原始消息相同。私钥加密即签名。
```
// 使用公钥加密:
let enc_by_pub = crypto.publicEncrypt(pubKey, Buffer.from(message, 'utf8'));
console.log('encrypted by public key: ' + enc_by_pub.toString('hex'));

// 使用私钥解密:
let dec_by_prv = crypto.privateDecrypt(prvKey, enc_by_pub);
console.log('decrypted by private key: ' + dec_by_prv.toString('utf8'));
```
执行后，可以得到解密后的消息，与原始消息相同。

因为RSA加密的原始信息必须小于Key的长度，RSA并不适合加密大数据。  
最佳实践：生成一个随机的AES密码，用AES加密原始信息，然后用RSA加密AES口令。实际给对方传的密文分两部分，一部分是AES加密的密文，另一部分是RSA加密的AES口令。对方用RSA先解密出AES口令，再用AES解密密文，即可获得明文。