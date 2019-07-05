# Linux下安装 [translate-shell]

## 基于cli的终端应用

- 占用内存和其他系统资源更少，对低配置的电脑很友好

## 下载最新版本

```bash
wget git.io/trans
```

## 修改(文件或者目录)权限

```bash
chmod +x ./trans
```

## 移动(文件或者目录)到/opt下

```s
sudo mv trans /opt/trans
```

## 创建终端下的快速启动命令

```s
sudo ln -s /opt/trans /usr/bin/trans
```

## 通过终端来使用translate-shell，它会自动检测输入的语言，然后翻译成你的系统locate语言

---

[translate-shell]:https://github.com/soimort/translate-shell
