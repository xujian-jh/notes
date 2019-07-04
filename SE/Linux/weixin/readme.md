# Linux下安装微信

## 下载最新版本tar.gz压缩包

```s
wget https://github.com/geeeeeeeeek/electronic-wechat/releases/download/V2.0/linux-x64.tar.gz
```

## 解压压缩包

```s
sudo tar -zxvf linux-x64.tar.gz
```

## 把解压的文件夹放在/opt下

```s
sudo mv electronic-wechat-linux-x64/ /opt/electronic-wechat-linux-x64
```

## 创建终端下的快速启动命令

```s
sudo ln -s /opt/electronic-wechat-linux-x64/electronic-wechat /usr/bin/electronic-wechat
```

## 在桌面创建软链接

