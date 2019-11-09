#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/8 0008 下午 20:20 
# @Author : aiminhu
# @File : conMysql.py 
# @Software: PyCharm
import mysql.connector
'''
先用pip命令安装mysql-connector:python -m pip install mysql-connector
'''
mydb = mysql.connector.connect(
    host = 'localhost',  #数据库主机地址
    user = 'root' ,      #数据库用户名
    passwd = '123456',   #数据库密码
    database = 'test_db' #直接连数据库，如果数据库没有会报错
)
# print(mydb)

#创建数据库
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES") #查看所有的数据库
# mycursor.execute("CREATE DATABASE test_db") #创建数据库，若是数据库已存在会报错

#创建数据表
# mycursor.execute("SHOW TABLES") #查看所有表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255),url VARCHAR(255))") #创建表，字段为name 和 url

#添加主键
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#创建表的同时添加主键
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),url VARCHAR(255))")

#

