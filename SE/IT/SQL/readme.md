# CRDBMS (Relational Database Management System)

获得绝对市场份额

## 关系模型

把数据看作是一个二维表格，任何数据都可以通过行号+列号来唯一确定

RDBMS是E.F.Codd博士在其发表的论文《大规模共享数据银行的关系型模型》(Communications of the ACM杂志1970年6月刊)基础上设计出来的

## 主流的RDBMS

- 商用数据库，例如：Oracle，SQL Server，DB2等
- 开源数据库，例如：MySQL，PostgreSQL等
- 桌面数据库，例如：Access等
- 嵌入式数据库，例如：Sqlite等

## RDBMS的特点

- 数据以表格的形式出现
  - 每行为各种记录名称
  - 每列为记录名称所对应的数据域
- 许多的行和列组成一张表单（tables）
- 若干的表单组成database

## 标准SQL

- 理论上所有RDBMS都可以支持
- 2016年12月14日,ISO/IEC发布了最新版本的数据库语言SQL标准(ISO/IEC 9075:2016)

## 扩展SQL

- 换一个数据库就不能执行，通常我们把它们称之为“方言”
- 某个特定数据库
  - Oracle把自己扩展的SQL称为`PL/SQL`
  - Microsoft把自己扩展的SQL称为`T-SQL`

## SQL (Structured Query Language)

- DDL (Data Definition Language)
  - DDL允许用户定义数据，也就是创建表、删除表、修改表结构这些操作
  - 通常，DDL由数据库管理员执行
- DML (Data Manipulation Language)
  - DML为用户提供添加、删除、更新数据的能力
  - 这些是应用程序对数据库的日常操作
- DQL (Data Query Language)
  - DQL允许用户查询数据
  - 这也是通常最频繁的数据库日常操作

## MySQL

- MySQL是目前应用最广泛的开源关系数据库
  - MariaDB：由MySQL的创始人创建的一个开源分支版本，使用XtraDB引擎
  - Aurora：由Amazon改进的一个MySQL版本，专门提供给在AWS托管MySQL用户，号称5倍的性能提升
  - PolarDB：由Alibaba改进的一个MySQL版本，专门提供给在阿里云托管的MySQL用户，号称6倍的性能提升
- MySQL本身实际上只是一个SQL接口，它的内部还包含了多种数据引擎
- MySQL官方版本又分了好几个版本，功能依次递增（功能增加的主要是监控、集群等管理功能），价格也依次递增
  - Community Edition：社区开源版本，免费
  - Standard Edition：标准版
  - Enterprise Edition：企业版
  - Cluster Carrier Grade Edition：集群版
