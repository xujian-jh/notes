# 关于版本问题

1、接口服务器  
（1）物料拉动程序：

- 刘英杰提交的最终版源码没有发布，源码在文件服务器MES交付物文档
- 目前在用的版本是将172.20.81.26上发布的war包下载下来反编译后，修改了工作日历读取时间（可能改到了30天or 60天？），然后重新发布了war包，相对应的源码需要问下汪敏。

（2）装配单打印

- 刘英杰提交的最终版在文件服务器MES交付文档
- 现在使用的war包，是在原来代码的基础上修改增加了一个字段显示后重新生成的，相对应的源码时间太长不记得了，这个没啥影响。

2、管理端  
（1）生产订单的VIN码重置、删除等逻辑微调了一下，有代码服务器：172.20.11.245
