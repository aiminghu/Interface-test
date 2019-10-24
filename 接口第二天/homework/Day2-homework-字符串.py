#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/18 0018 下午 17:17 
# @Author : aiminhu
# @File : Day2-homework-字符串.py
# @Software: PyCharm
'''
有这样一个文件，文件内容如下：
Lucy|18601914231|男|19890218
Jack|18101913132|女|19810311
Tom|18201912533|女|19830713
Lily|18301911734|男|19870210

任务1-找出所有L开头的人名
任务2-按照年龄进行排序
任务3-找出所有女性用户的信息

'''

with open('E:\新建文件夹\zuoye\接口第二天\data1.txt','r',encoding='utf-8') as read_file:
    files = read_file.readlines()
    # 读取文件全部内容
l = []
for i in files:
    l.append(i.replace('\n',''))
# print(l)
data = []
for i in range(len(l)):
    data = data + l[i].split('|')

# 任务1-找出所有L开头的人名
name = []
for i in data:
    if i.startswith('L'):
        name.append(i)
print('文件中L开头的人名有：',name)

# 任务2-按照年龄进行排序
age = []
for i in l:
    age.append(i)
print(age)
for i in range(len(age)):
    if i <=len(l):
        a=int(age[i][-8:-1:])
        b = int(age[i+1][-8:-1:])
        print(a,b)
        if a < b: #判断年龄大小然后交换数据，index超出范围
            c = age[i]
            age[i] = age[i+1]
            age[i+1] = c



print(age)
