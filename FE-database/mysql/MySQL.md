pre

database的理论知识会在tws的文件中进行补充，课上的理论知识内容也会放在那个文件中。

[tws-databases](/Users/xusumu/OneDrive/1.notes/2.FE/2.thoughtworks/database/database-thoughtworks.md)

  1、sql不区分大小写  预定俗称的规定  自己取得名字小写  系统的大写

  2、每一句话都必须加分好

[MySQL Tutorial](https://www.w3schools.com/mysql/default.asp)

# 1. Installation(for Mac)

**2021,讲课时用5.6/5.7的版本，因为8.0的版本和5的版本连语法都已经不一样了**

1. 下载地址：[download MySQL](http://dev.mysql.com/downloads/mysql/)

**下载5.6/5.7的版本即可**

2. Open MySQL System Preferences
3. MySQL System Preferences
4. Start MySQL

![MySQL System Preferences](https://www.quackit.com/pix/mysql/tutorial/mysql_5-6_installation/mysql_installation_11.png)

![Start MySQL](https://www.quackit.com/pix/mysql/tutorial/mysql_5-6_installation/mysql_installation_12.png)

## terminal start

```sql
// 进入mysql（要求输入mysql登录密码）
mysql -u root -p
// 退出mysql
exit
```

![7A13DC266631C626B698F68369713A72.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gr2ipgfzxdj60vi0hatc402.jpg)

# 2. MySQL Workbench

[6.3.10 ver](https://downloads.mysql.com/archives/workbench/)

# 3. 如何运行代码

1. 这个⚡️按钮点击实现运行所有代码够功能
2. ⚡️旁边的按钮有个输入标签的，表示只运行某一行代码
3. You can also run a query by selecting Query | Execute (All or Selection) (or one of the alternative options).
4. 快捷键 for mac : command + enter , Execute (All or Selection).

## comment

```sql
/*
  多行注释
  1、sql不区分大小写  预定俗称的规定  自己取得名字小写  系统的大写
  2、每一句话都必须加分好
*/

-- 单行注释
```

## semicolons

**结束语句一定要写分号作为结尾**

# 4. Naming Conventions

命名习惯

`FruitShop` (title case), `FRUITSHOP` (uppercase), `fruitshop` (lowercase), `fruit_shop` (with an underscore separator), etc.

prefixing tables is ok with `tbl` or `tbl_` and stored procedures with `sp` or `sp_`. So a table could be called `tblCustomers` or `tbl_customers` etc.

Whichever you choose, you should try to maintain the same convention throughout your database.

# 5. Create/modify a Database

```sql
CREATE DATABASE db_name;
```

```sql
CREATE DATABASE FruitShop;
CREATE SCHEMA FruitShop;
-- 相同的创建数据效果，一般使用第一个
```

```sql
SHOW DATABASES;
--显示所有服务器中的数据

--如果不存在则创建，因为数据库中不能存在同名的表格，创建同名表格会报错
CREATE DATABASE IF NOT EXISTS FruitShop;

--删除老的同名数据，并创建新的同名数据
DROP DATABASE IF EXISTS FruitShop;
CREATE DATABASE FruitShop;
```

```sql
ALTER DATABASE
```

Using the above `IF NOT EXISTS` is great as long as you have no intention of replacing the database (and all its data) with a fresh new one. But sometimes you might want to delete the old database and start again from scratch. This is where `DROP DATABASE` comes in handy.

# 6. table 操作

## switch database

```sql
use test;

use onlineappointment;
```



## 展示所有数据库

```sql
show databases;
```



## a. Create a Table

```sql
create table 表名(
	列名 列的数据类型 [列的约束],
	列名 列的数据类型 列的约束]
	...
)
```

```sql
CREATE TABLE Fruit (FruitName VARCHAR(20), DateEntered DATETIME);

CREATE TABLE t_user(
	u_id INT PRIMARY KEY AUTO_INCREMENT,
	u_num CHAR(6) UNIQUE NOT NULL,
	u_name VARCHAR(6) NOT NULL,
	u_sex CHAR(1) DEFAULT "女",
	u_age INT,
	u_enter_school DATE	
)

CREATE TABLE Units (
UnitId TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
UnitName VARCHAR(10) NOT NULL,
DateEntered DATETIME NOT NULL,
DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (UnitId)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Fruit (
FruitId SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
FruitName VARCHAR(45) NOT NULL, 
Inventory SMALLINT UNSIGNED NOT NULL,
UnitId TINYINT UNSIGNED NOT NULL,
DateEntered DATETIME NOT NULL,
DateUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (FruitId),
CONSTRAINT fkFruitUnits FOREIGN KEY (UnitId) REFERENCES Units (UnitId) ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

### 数据类型

1. 主键约束   每个表都应该有主键约束  保证每一条数据都不一样 唯一且不为空  primary key
2. 唯一约束   唯一可以为空 unique
3. 非空约束   不能为空 not null
4. 默认值 default
5. 自增  长和主键一起使用 auto_increment
6. [外键约束 ](# 9. Foreign Key)

[runoob 数据类型](https://www.runoob.com/mysql/mysql-data-types.html)

[Chapter 11 Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

### 数值类型

| 类型         | 范围（无符号）                                               | 用途            |
| :----------- | :----------------------------------------------------------- | :-------------- |
| TINYINT      | (0，255)                                                     | 小整数值        |
| SMALLINT     | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 依赖于M和D的值                                               | 小数值          |
| unsigned     |                                                              | 非负数          |

### 日期和时间类型

| 型        | 大小 ( bytes) | 范围                                                         | 格式                | 用途                     |
| :-------- | :------------ | :----------------------------------------------------------- | :------------------ | :----------------------- |
| DATE      | 3             | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3             | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1             | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8             | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| TIMESTAMP | 4             | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

### 字符串类型

| 类型       | 大小                  | 用途                            |
| :--------- | :-------------------- | :------------------------------ |
| CHAR       | 0-255 bytes           | 定长字符串                      |
| VARCHAR    | 0-65535 bytes         | 变长字符串                      |
| TINYBLOB   | 0-255 bytes           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255 bytes           | 短文本字符串                    |
| BLOB       | 0-65 535 bytes        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535 bytes        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215 bytes    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215 bytes    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295 bytes | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295 bytes | 极大文本数据                    |

###  char、varchar 与 text 

关于 char、varchar 与 text 平时没有太在意，一般来说，可能现在大家都是用 varchar。但是当要存储的内容比较大时，究竟是选择 varchar 还是 text 呢？

这三种类型比较：

-  （1）**char**:  char 不用多说了，它是定长格式的，但是长度范围是 0~255. 当你想要储存一个长度不足 255 的字符时，Mysql 会用空格来填充剩下的字符。MySQL在存储char的时候，先去掉尾部的空格，若长度不足则用空格填充到相应长度。查询时，返回的数据尾部是没有空格的。
-  （2）**varchar**:  关于 varchar，有的说最大长度是 255，也有的说是 65535，查阅很多资料后发现是这样的：varchar 类型在 5.0.3 以下的版本中的最大长度限制为 255，而在 5.0.3 及以上的版本中，varchar 数据类型的长度支持到了 65535，也就是说可以存放 65532 个字节（注意是字节而不是字符！！！）的数据（起始位和结束位占去了3个字节），也就是说，在 5.0.3 以下版本中需要使用固定的 TEXT 或 BLOB 格式存放的数据可以在高版本中使用可变长的 varchar 来存放，这样就能有效的减少数据库文件的大小。
-  （3）**text**: 与 char 和 varchar 不同的是，text 不可以有默认值，其最大长度是 2 的 16 次方-1

**总结起来，有几点：**

-  经常变化的字段用 varchar
-  知道固定长度的用 char
-  尽量用 varchar
-  超过 255 字符的只能用 varchar 或者 text
-  能用 varchar 的地方不用 text

### 约束词

### Display Table Information Programatically

```sql
-- set the default database to be FruitShop by using USE FruitShop
USE FruitShop;

--ask MySQL to display all tables for the default database
SHOW TABLES;

--find out the structure of a given table by using the following command (simply replace the table name with the table you need the structure of):
DESCRIBE Fruit;
```

![DESCRIBE Fruit](https://www.quackit.com/pix/mysql/tutorial/create_table/mysql_create_table_2.png)



## b. Delete table

```sql
CREATE TABLE t_user(
	u_id INT PRIMARY KEY AUTO_INCREMENT,
	u_num CHAR(6) UNIQUE NOT NULL,
	u_name VARCHAR(6) NOT NULL,
	u_sex CHAR(1) DEFAULT "女",
	u_age INT,
	u_enter_school DATE,
	u_c_id INT,
	CONSTRAINT FOREIGN KEY(u_c_id) REFERENCES t_classroom(c_id)	  
);

DROP TABLE t_user;
```

## c. Insert column 

```sql
ALTER TABLE t_user ADD tel CHAR(11) NOT NULL;
```

## d. Delete column

```sql
-- alter table 表名 drop 列名
ALTER TABLE t_user DROP tel;
```

## e. Update/modify table

```sql
-- alter table 表名 change 老的列名  新的列名 数据类型 [约束];
ALTER TABLE t_user CHANGE u_num u_no INT UNIQUE;
```
## f. select data

```sql
-- 筛选出column1, column2这两列内容 从table_name中
SELECT column1, column2, ...
FROM table_name;
-- 从table_name中获取表格所有数据
SELECT * FROM table_name;
```



# 7. data 操作

## a. Insert Data

1. 主键默认自增用 null 
2. 如果想要用默认default\
3. 第一个括号里面可以改变顺序，第二个括号按照这个顺序走
4. 如果有可以为空的不想写，第一个括号可以不写
5. 加入第一个括号里面的所有都不写（没有第一个括号） 第二个括号按照表的顺序，一次添加

```sql
--插入对应列，值与表格名一一对应
INSERT INTO table_name (col_1, col_2, col_3) 
VALUES (value_1, value_2, value_3);

--inserting data into all columns，omit the column names
INSERT INTO table_name VALUES (value_1, value_2, value_3);

--可以换行，用逗号分隔每个值
INSERT INTO table_name 
VALUES 
(value_1, value_2, value_3),
(value_1, value_2, value_3),
(value_1, value_2, value_3),
(value_1, value_2, value_3);
```

```sql
INSERT INTO Units 
VALUES 
(1,'Piece','2015-02-15 10:30:00','2015-02-15 10:30:00'),
(2,'Kilogram','2015-02-15 10:30:00','2015-02-15 10:30:00'),
(3,'Gram','2015-02-15 10:30:00','2015-02-15 10:30:00'),
(4,'Pound','2015-02-15 10:30:00','2015-02-15 10:30:00'),
(5,'Ounce','2015-02-15 10:30:00','2015-02-15 10:30:00'),
(6,'Bunch','2015-02-15 10:30:00','2015-02-15 10:30:00'),
(7,'Container','2015-02-15 10:30:00','2015-02-15 10:30:00');
	
INSERT INTO Fruit 
VALUES 
(1,'Apple',10,1,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(2,'Orange',5,2,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(3,'Banana',20,6,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(4,'Watermelon',10,1,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(5,'Grapes',15,6,'2015-02-15 10:30:00','2015-02-15 10:30:00'),
(6,'Strawberry',12,7,'2015-02-15 10:30:00','2015-02-15 10:30:00');

INSERT INTO t_user(u_id,u_num,u_name,u_sex,u_age,u_enter_school,u_c_id) 
VALUES(NULL,'12','aa',DEFAULT,12,'2021-02-02',1);

INSERT INTO t_classroom (c_name,c_id) VALUES('三年一班',NULL);

INSERT INTO t_user(u_num,u_name,u_age) VALUES('aaa','aaa',12);

INSERT INTO t_user VALUES(NULL,'bbb','bbb','男',12,'2021-01-01',2);
```

## b. Check your Data

Check the Fruit Table

```sql
select * from Fruit
```

![Check the Fruit Table](https://www.quackit.com/pix/mysql/tutorial/insert_data/mysql_insert_data_1.png)

## c. Queries

```sql
--The asterisk (*) tells MySQL to return all columns.
SELECT * FROM Fruit;

--return only those columns that you want to return. 
SELECT FruitId, FruitName 
FROM Fruit;

SELECT * FROM Fruit
WHERE UnitId = 1;

SELECT * FROM Fruit
WHERE UnitId = 
	(SELECT UnitId 
    FROM Units 
    WHERE UnitName = 'Piece');
```

![return only those columns that you want to return](https://www.quackit.com/pix/mysql/tutorial/mysql_queries/mysql_query_example_2.png)



![](https://www.quackit.com/pix/mysql/tutorial/mysql_queries/mysql_query_example_3.png)

## d. Update Data

```sql
-- update 表名 set 列名=值; 修改整个一列的值
-- update 表名 set 列名=值 [where 条件名=条件值];
```

```sql
--Update a Data
UPDATE Fruit
SET UnitId = 2
WHERE FruitId = 1;

--Update Multiple Fields
UPDATE Fruit
SET FruitName = 'Red Grapes', Inventory = '11'
WHERE FruitId = 5;
```

### Safe Updates mode

开启安全更新模式会防止我们错误更新表格

```sql
--会将所有内容修改成banana
UPDATE Fruit
SET FruitName = 'Banana'
```

```sql
--开启
set sql_safe_updates = 1;
--禁止
set sql_safe_updates = 0;
```

```sql
--As it turns out, I was only able to run the above statement after disabling Safe Updates mode. So, before I ran that statement, I ran the following command:

set sql_safe_updates = 0;

UPDATE Fruit
SET UnitId = 2
WHERE FruitName = 'Apple';

select * from Fruit;

set sql_safe_updates = 1;
```

## e. Delete Data

### delete data

```sql
--Delete some Data
DELETE
FROM table_name
WHERE column_name = value;

--Delete All Records
DELETE FROM Fruit;

--彻底删除
TURNCATE tableNAME

--同时删除多个
DELETE FROM t_shop WHERE s_id in(4,9,1);

-- 平常咱们都用第一种。第一种普通删除，虽然删除了，但是数据库有记录，可以恢复。
-- 第二种删除不能恢复的。我们一般在项目上线前，把测试数据全部删除掉。也叫洗表
```

### SAFE DELETE

```SQL
set sql_safe_updates = 0;

DELETE
FROM Fruit
WHERE FruitId = 5;

select * from Fruit;

set sql_safe_updates = 1;
```

## e. PRIMARY KEY

![](https://www.quackit.com/pix/mysql/tutorial/primary_key/mysql_primary_key_1.png)

## 添加主键的三种方法

```sql
-- 1、 create table 表名(列名 数据类型 primary key)
CREATE TABLE t_user(
	u_id INT PRIMARY KEY AUTO_INCREMENT
)
-- 2、 可以添加联合主键
CREATE TABLE t_user(
	u_id INT  AUTO_INCREMENT,
	u_num CHAR(6) UNIQUE NOT NULL,
	u_name VARCHAR(6) NOT NULL,
	u_sex CHAR(1) DEFAULT "女",
	u_age INT,
	u_enter_school DATE,
	PRIMARY KEY(u_id)	
)
-- 3、
CREATE TABLE t_user(
	u_id INT  AUTO_INCREMENT,
	u_num CHAR(6) UNIQUE NOT NULL,
	u_name VARCHAR(6) NOT NULL,
	u_sex CHAR(1) DEFAULT "女",
	u_age INT,
	u_enter_school DATE	
)
ALTER TABLE t_user CHANGE u_id u_id INT PRIMARY KEY  AUTO_INCREMENT;
```

## f. Foreign Key

外键约束(Foreign Key Constraint)

1. 一个表的外键要链接另一张表的主键
2. 链接主键的表是主表，外键的那张表是从表，从表的内容在主表里面选
3. 创建表的时候，因为先创建主表，在创建从表   
4. 删除表的时候，先删除从表，再删主表

A foreign key is a column (or collection of columns) in one table that uniquely identifies a row of another table. This defines a relationship between the two tables.

![Foreign Key](https://www.quackit.com/pix/mysql/tutorial/foreign_key/mysql_foreign_key_1.png)

The UnitId field on the Fruit table is a foreign key to the UnitId field on the Units table. 

### The Data

Units table为主表， Fruit table 为从表。

So if our Fruit table contains a record like this:

| FruitId | FruitName | Inventory | UnitId | DateEntered         | DateUpdated         |
| ------- | --------- | --------- | ------ | ------------------- | ------------------- |
| 1       | Apple     | 10        | 3      | 2012-11-27 12:42:10 | 2012-11-27 12:42:10 |

And our Units table contains the following records:

| UnitId | UnitName  | DateEntered         | DateUpdated         |
| ------ | --------- | ------------------- | ------------------- |
| 1      | Piece     | 2011-12-30 12:46:15 | 2011-12-30 12:46:15 |
| 2      | Bunch     | 2011-12-30 12:46:15 | 2011-12-30 12:46:15 |
| 3      | Kilogram  | 2011-12-30 12:46:15 | 2011-12-30 12:46:15 |
| 4      | Container | 2011-12-30 12:46:15 | 2011-12-30 12:46:15 |
| 5      | Pound     | 2011-12-30 12:46:15 | 2011-12-30 12:46:15 |
| 6      | Ounce     | 2011-12-30 12:46:15 | 2011-12-30 12:46:15 |

You can see that the Fruit.UnitId field contains a `3`. Now look at the Units table for the record that contains a `3` in the UnitId field. You can see that this record represents Kilogram. Therefore, we now know that apples are measured in kilograms.

### Foreign Key Constraint

```sql
CONSTRAINT fkFruitUnits FOREIGN KEY (UnitId) REFERENCES Units (UnitId) ON DELETE RESTRICT ON UPDATE CASCADE
```

```sql
--主表
CREATE TABLE t_classroom(
	c_id INT PRIMARY KEY AUTO_INCREMENT,
	c_name VARCHAR(10)
)

--从表
CREATE TABLE t_user(
	u_id INT PRIMARY KEY AUTO_INCREMENT,
	u_num CHAR(6) UNIQUE NOT NULL,
	u_name VARCHAR(6) NOT NULL,
	u_sex CHAR(1) DEFAULT "女",
	u_age INT,
	u_enter_school DATE,
	u_c_id INT,
	CONSTRAINT FOREIGN KEY(u_c_id) REFERENCES t_classroom(c_id)	  
)
```



## g. Query 

### 1. 查找对应列内容 select from

```sql
-- select 列名,列名,* from 表名;
SELECT u_age FROM t_user;	 
SELECT u_name,u_age FROM t_user;
SELECT * FROM t_user;
```

### 2. 修改列名select as/Aliases

```sql
SELECT u_name AS NAME,u_age AS age FROM t_user;
SELECT u_name NAME,u_age age FROM t_user;  
-- 前期 AS 不建议省略

-- 只是在筛选出来的时候用新的列名，但是原始列名不会被修改

SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;
```

### 3. 统一修改某列数值

```sql
SELECT u_age+5 AS age FROM t_user;
```

### 4. 去重 distinct

```sql
SELECT DISTINCT u_age FROM t_user;
SELECT DISTINCT u_name, u_age FROM t_user;
```

### 5. limit

```sql
SELECT * FROM t_user LIMIT 1,3;
SELECT * FROM table LIMIT 5,10; 
-- 检索记录行 6-15 
-- 换句话说，LIMIT n 等价于 LIMIT 0,n
```

### 6. 条件查询 where

```sql
SELECT * FROM t_user WHERE u_id=10;
```

### 7. 范围查询 and or not

and or between

```sql
SELECT * FROM t_user WHERE u_id>=6 AND u_id<=10;

SELECT * FROM t_user WHERE u_id=2 OR u_id=8;

SELECT * FROM t_user WHERE u_id BETWEEN 2 AND 8;

SELECT * FROM Customers
WHERE NOT Country='Germany';
```

### 8. 模糊查询 % _

- % 代表任意长度的字符

- _ 代表是单个长度的字符

```sql
SELECT * FROM t_user WHERE u_name LIKE '%a%';
SELECT * FROM t_user WHERE u_name LIKE '___a';
```

| LIKE Operator                  | Description                                                  |
| :----------------------------- | :----------------------------------------------------------- |
| WHERE CustomerName LIKE 'a%'   | Finds any values that start with "a"                         |
| WHERE CustomerName LIKE '%a'   | Finds any values that end with "a"                           |
| WHERE CustomerName LIKE '%or%' | Finds any values that have "or" in any position              |
| WHERE CustomerName LIKE '_r%'  | Finds any values that have "r" in the second position        |
| WHERE CustomerName LIKE 'a_%'  | Finds any values that start with "a" and are at least 2 characters in length |
| WHERE CustomerName LIKE 'a__%' | Finds any values that start with "a" and are at least 3 characters in length |
| WHERE ContactName LIKE 'a%o'   | Finds any values that start with "a" and ends with "o"       |

### 9. 非空查询

- is null     

- is not null
- 表里面的啥都没有是空字符串: ' '

```sql
SELECT * FROM t_user WHERE u_c_id IS NOT NULL;
SELECT * FROM t_user WHERE u_age='';
```

### 10. 排序 order by

查询后排序 order by  默认从小到大   desc 降序   asc升序

Descending，ascending

```sql
SELECT * FROM t_user ORDER BY u_age;
SELECT * FROM t_user ORDER BY u_age DESC;
SELECT * FROM t_user ORDER BY u_age,u_id DESC;
```

### 11. 聚合函数 min max avg sum count

<mark>将方法截图出来</mark>

- 主要方法：avg(列),max,min,sum,count(求总数)
-  聚合函数的特点
  1. 聚合函数查出来的都是单行单列
  2. 聚合函数查询不要和普通查询放在一起(一个是多行，一个是一行),导致查询失败
  3. 聚合方法可以多个一起使用可以一起查询
  4. 在计算的时候有null  如果有null 把他变成0  ifnull(列名,0)
  5. 聚合函数在使用的时候注意数据类型 ，最好是计算数值，计算时间会失败

```sql
-- 计算u_c_id有行，即有多少个数据
SELECT COUNT(u_c_id) FROM t_user;
SELECT COUNT(*) AS total FROM t_user;
--会在表格的最后创建新的一列
SELECT COUNT(1) FROM t_user;
SELECT MAX(u_age) FROM t_user;
SELECT MIN(u_age) FROM t_user;
SELECT AVG(u_age) FROM t_user;
SELECT SUM(u_age) FROM t_user;
SELECT u_name,MAX(u_age) FROM t_user;
SELECT COUNT(*),MAX(u_age)FROM t_user;
SELECT AVG(IFNULL(u_age,0)) FROM t_user;
SELECT AVG(u_enter_school) FROM t_user
```

### 12. 分组查询 group by

分组可以和聚合查询配合使用

The `GROUP BY` statement is often used with aggregate functions (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) to group the result-set by one or more columns.

```sql
SELECT u_c_id,COUNT(1) FROM t_user  GROUP BY u_c_id;
```

### 13. 筛选 having

```sql
SELECT u_c_id,COUNT(1) FROM t_user  GROUP BY u_c_id HAVING COUNT(1)>2;
```
### 14. count(*)

The `COUNT()` function returns the number of rows that matches a specified criterion.

count(*) 它返回检索行的数目， 不论其是否包含 NULL值。

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

SELECT 从一个表中检索，而不检索其它的列，并且没有 WHERE子句时， COUNT(*)被优化到最快的返回速度。

```sql
CREATE TABLE `user` (
  `id` int(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1

测试数据为：

--1 name1 123456
--2 name2 123456
--3 name3 123456
--4 name4  NULL

select count(*) from `user`
select count(name) from `user`
select count(password) from `user`

--输出结果：4,4,3
```

### 15. IN

selects all customers that are located in "Germany", "France" or "UK":

```sql
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
```

selects all customers that are not located in "Germany", "France" or "UK":

```sql
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');
```

### 16. null values

It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

### 17. 大小查询 min max <>...

<  >  <=  >=  =  != <> min max

## h. Joins

A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

### Supported Types of Joins in MySQL

- `INNER JOIN`: Returns records that have matching values in both tables
- `LEFT JOIN`: Returns all records from the left table, and the matched records from the right table
- `RIGHT JOIN`: Returns all records from the right table, and the matched records from the left table
- `CROSS JOIN`: Returns all records from both tables

![AE82395D62A649B980132A647BFB2C96.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gr40v8mig8j61ca09uwfz02.jpg)

### inner join

join 默认结果等于inner join 

![6A6271F4BEBD32CBC471243850EDE5BD.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gr40rcfvs6j61hu0wwgs302.jpg)

```sql
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
```

![B25AA04E-F6D0-4D19-BFBE-B70578B63280.png](http://ww1.sinaimg.cn/large/005NUwyggy1gr40trh10gj61lk0nwjvo02.jpg)

### right join

The `RIGHT JOIN` keyword returns all records from the right table (table2), and the matching records (if any) from the left table (table1).

```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

![82C01FA8144CFDA1F8F52FD518DB09A1.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gr4117avccj61iq0owtcp02.jpg)

### left join

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

The `LEFT JOIN` keyword returns all records from the left table (Customers), even if there are no matches in the right table (Orders).

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

```



![3A3816BD8E1862086436B82B9A4F04BA.jpg](http://ww1.sinaimg.cn/large/005NUwyggy1gr411upn6rj61j60t6n2g02.jpg)

### Cross join

**Note:** `CROSS JOIN` can potentially return very large result-sets!

```sql
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
```

## i. 复制表

### INSERT INTO SELECT

Copy all columns from one table to another table:

```sql
INSERT INTO table2
SELECT * FROM table1
WHERE condition;
```

Copy only some columns from one table into another table:

```sql
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;
```

### SELECT INTO

The `SELECT INTO` statement copies data from one table into a new table.

```sql
-- Copy all columns into a new table:
SELECT *
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```

```sql
-- Copy only some columns into a new table:
SELECT column1, column2, column3, ...
INTO newtable [IN externaldb]
FROM oldtable
WHERE condition;
```

```sql
-- The following SQL statement uses the IN clause to copy the table into a new table in another database:

SELECT * INTO CustomersBackup2017 IN 'Backup.mdb'
FROM Customers;

-- The following SQL statement copies only a few columns into a new table:
SELECT CustomerName, ContactName INTO CustomersBackup2017
FROM Customers;
```

**Tip:** `SELECT INTO` can also be used to create a new, empty table using the schema of another. Just add a `WHERE` clause that causes the query to return no data:

```sql
SELECT * INTO newtable
FROM oldtable
WHERE 1 = 0;
```

## j. EXISTS

The `EXISTS` operator is used to test for the existence of any record in a subquery.

The `EXISTS` operator returns TRUE if the subquery returns one or more records.

```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```

## k. any all

The `ANY` operator:

- returns a boolean value as a result
- returns TRUE if ANY of the subquery values meet the condition

**Note:** The *operator* must be a standard comparison operator (=, <>, !=, >, >=, <, or <=).

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
  (SELECT column_name
  FROM table_name
  WHERE condition);
```

The `ALL` operator:

- returns a boolean value as a result
- returns TRUE if ALL of the subquery values meet the condition
- is used with `SELECT`, `WHERE` and `HAVING` statements

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator ALL
  (SELECT column_name
  FROM table_name
  WHERE condition);
  
SELECT ALL column_name(s)
FROM table_name
WHERE condition;
```

```sql
SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
  
SELECT ProductName
FROM Products
WHERE ProductID = ANY (SELECT ProductID FROM OrderDetails WHERE Quantity > 99);
```



# 8. sql语句的执行顺序

from>where>select>grounp by> 聚合函数>having> 排序>limit

```sql
SELECT 去重 列名|*|聚合喊出
FROM 表名
WHERE
GROUP BY 
HAVING 	
ORDER BY
LIMIT 
```

```sql
-- from 先去找对应的表
-- where 根据条件把符合条件的找出来
-- select 看需要哪些列
-- group by  进行分组
-- 统计
-- 进行过滤
-- 排序
-- limit 
-- 返回的数据最终计算

SELECT *
FROM t_user
WHERE u_age IS NOT NULL
ORDER BY u_age DESC
LIMIT 0,5

select itemId as 商品编号,salesSum as 销售总金额 ,staff as 销售人员 from salesRecord  where staff="王五" limit 0,5;
```

# error collection

## error 1215

1. MySQL中创建外键的错误：1215 Cannot add the foreign key constraint

之所以出现1215的问题，是由于主外键之间的数据类型不一致造成的，以后类似问题，皆可按此处理。

## 修改字符集

[mac 设置 MySQL 数据库默认编码（字符集）为 UTF-8](https://juejin.cn/post/6844903688977252360)

[修改mysql密码](https://juejin.cn/post/6844904064904331272)

Limit , 联合主键 ,11. 聚合函数，复制表格

## Error 1248. 

Every derived table must have its own alias

这句话的意思是说每个派生出来的表都必须有一个自己的别名。嵌套查询的时候子查询出来的结果是作为一个派生表来进行上一级的查询的，所以子查询的结果必须要有一个别名。

select class,count(1) as 班级人数,sum(score) as 班级总分,avg(score) as 班级平均分, max(score) as 班级最高分,min(score) as 班级最低分 from (select * from pracs3 where class="T01") as group by class;

改为

select class,count(1) as 班级人数,sum(score) as 班级总分,avg(score) as 班级平均分, max(score) as 班级最高分,min(score) as 班级最低分 from (select * from pracs3 where class="T01") as table2 group by class;