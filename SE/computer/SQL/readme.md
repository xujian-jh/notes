# [SQL] (Structured Query Language)

>SQL是最重要的关系数据库操作语言，用于存取数据以及查询、更新和管理关系数据库系统。

>SQL于1986年10月由美国国家标准局（ANSI）通过的数据库语言美国标准。1987年国际标准化组织（ISO）颁布了SQL正式国际标准。1989年4月ISO提出了具有完整性特征的SQL89标准。1992年11月ISO又公布了SQL92标准，在此标准中，把数据库分为三个级别：基本集、标准集和完全集。

>SQL基本上是域关系演算，但可以实现关系代数操作。SQL语言是一种交互式查询语言，允许用户直接查询存储数据，但它不是完整的程序语言，如它没有DO或FOR 类似的循环语句，但它可以嵌入到另一种语言中，也可以借用VB、C、JAVA等语言，通过调用级接口（CALL LEVEL INTERFACE）直接发送到数据库管理系统。SQL语言基本上独立于数据库本身、使用的机器、网络、操作系统。

#### DQL (Data Query Language)

>用以从表中获得数据。保留字SELECT，WHERE，ORDER BY，GROUP BY和HAVING。这些DQL保留字常与其他类型的SQL语句一起使用。

#### DML (Data Manipulation Language)

>其语句包括动词INSERT，UPDATE和DELETE。它们分别用于添加，修改和删除表中的行。

#### TPL (Transaction Processing Language)

>它的语句能确保被DML语句影响的表的所有行及时得以更新。TPL语句包括BEGIN TRANSACTION，COMMIT和ROLLBACK。

#### DCL (Data Control Language)

>它的语句通过GRANT或REVOKE获得许可，确定单个用户和用户组对数据库对象的访问。某些RDBMS可用GRANT或REVOKE控制对表单个列的访问。

#### DDL (Data Definition Language)

>其语句包括动词CREATE和DROP。在数据库中创建新表或删除表（CREAT TABLE 或 DROP TABLE）；为表加入索引等。DDL包括许多与人数据库目录中获得数据有关的保留字。它也是动作查询的一部分。

#### CCL (Cursor Control Language)

>它的语句，像DECLARE CURSOR，FETCH INTO和UPDATE WHERE CURRENT用于对一个或多个表单独行的操作。




[SQL]:https://baike.baidu.com/item/%E7%BB%93%E6%9E%84%E5%8C%96%E6%9F%A5%E8%AF%A2%E8%AF%AD%E8%A8%80/10450182?fr=aladdin