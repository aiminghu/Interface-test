#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/14 0014 上午 10:16 
# @Author : aiminhu
# @File : conMysql_1.py 
# @Software: PyCharm
import pymysql

#链接database
conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root', password = '123456',
    database='test_db',
)

#得到一个可以执行sql语句的光标对象
cursor = conn.cursor() #执行完毕返回的结果集默认以元祖显示
#得到一个可以执行SQl语句并且将结果作为字典返回的游标
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#
#定义要执行的SQL语句
sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;  #注意：charset='utf8' 不能写成utf-8
"""

#注意：charset='utf8' 不能写成utf-8

#执行SQL语句
cursor.execute(sql)

#关闭光标对象
cursor.close()

#关闭数据库连接
conn.close()
