#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/13 0013 下午 15:37 
# @Author : aiminhu
# @File : lx2.py 
# @Software: PyCharm
'''
文件IO
'''
#读取txt中的数字，按照从小到大的顺序写入另一个文件
#思路：1、读取文件中的内容  2、对读取出来的结果排序（a.去除\n  b.对新列表进行排序） 3、将排序后的结果写入新的文件
f = open('E:\新建文件夹\zuoye\接口第二天\\num.txt', 'r')
# print(f.readline())
a = f.readlines()  #读取文件中的数字
b = []
for line in a:
    line = line.strip() #去除'\n',换行
    b.append(int(line)) #变成int类型，放入新的数组
# print(b)
# b.sort()   #sort()方法没有返回值，直接改变原数组；sorted()有返回值
# print(b)
c = sorted(b) #排序，
# print(c)
d = []
file = open('E:\新建文件夹\zuoye\接口第二天\\num_1.txt', 'w+')
for i in c:
    i = str(i) #转换成字符串，放入新数组
    d.append(i)
for j in d:
    file.write(j) #逐个写入新文件
    file.write('\n')
f.close()
file.close()

# def readtxt():
#     with open('E:\新建文件夹\zuoye\接口第二天\\num.txt', 'r') as f:

