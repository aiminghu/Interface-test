#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/18 0018 下午 17:17 
# @Author : aiminhu
# @File : Day2-1.py 
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

print(files)