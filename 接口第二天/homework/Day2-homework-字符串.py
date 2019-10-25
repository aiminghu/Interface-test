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
# 任务1-找出所有L开头的人名
with open('../data1.txt','r',encoding='utf-8') as read_file:
    data = read_file.readlines()
    # 读取文件全部内容
    name = []
    for i in data:
        i = i.replace('\n','')
        li = i.split('|')[0]
        if li.startswith('L'):
            name.append(li)
    print('文件中L开头的人名有：',name)


# 任务2-按照年龄进行排序
str_list = []
with open('../data1.txt','r+',encoding='utf-8') as f:
    for i in f.readlines():
        i = i.strip('\n')
        str_list.append(i)
    # print(str_list)
li = sorted(str_list,key=lambda x:x[-8:])
print(li)
'''
#返回一个元祖，排列顺序为：先对比所有元祖的第一个元素，在对比第二个。
# reverse参数为False，为升序排列
key=lambda 元素: 元素[字段索引]
比如   print(sorted(C, key=lambda x: x[2]))   
x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序
'''
# 任务3-找出所有女性用户的信息
famale = []
with open('../data1.txt','r+',encoding='utf-8') as f:
    data = f.readlines()
    for i in data:
        # print(i.split('|')[2])
        if i.split('|')[2] == '女':
            famale.append(i)
    print("文件中女性用户的信息为:",famale)
