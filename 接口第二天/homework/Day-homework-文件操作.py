#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/24 0024 下午 20:43 
# @Author : aiminhu
# @File : Day-homework-文件操作.py 
# @Software: PyCharm
import os
import shutil
# print(os.getcwd()) #返回当前工作目录
path = os.getcwd()
os.listdir(path) #返回指定文件夹中包含的文件或文件夹的名字的列表
# print(os.listdir('E:\新建文件夹\zuoye\接口第二天'))#返回path制定文件夹包含的文件或文件夹的名称
# os.makedirs('E:\新建文件夹\zuoye\接口第二天\wenjian') #递归文件夹创建函数
# os.remove(path)  #删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory
# os.removedirs(path) #递归删除目录
# os.rename('hello','wenjian') #重命名文件或目录
# os.rmdir('E:\新建文件夹\zuoye\接口第二天\wenjian') #删除path指定的空目录，如果目录非空，则抛出一个OSError异常
# print(os.path.abspath(path)) #返回绝对路径
# print(os.path.basename(path)) #返回文件名
# print(os.path.dirname(path)) #返回文件夹路径
os.path.exists(path) #路径存在返回True，路径损坏返回False
os.path.isfile(path) #判断路径是否为文件
# print(os.path.isdir(path)) #判断文件是否为目录
# os.path.join(path1,path2) #把文件夹和目录合成一个目录
os.path.realpath(path) #返回path的真实路径
# os.path.samefile(path1,path2) #判断目录或文件是否相同
# print(os.path.split(path)) #把路径分割成敌人dirname和basename,返回一个元祖
# print(os.path.splitext(path)) #分隔路径，返回路径名和文件扩展名的元祖
'''
练习：
目录下有这些文件：
A1.txt
B2.txt
C1.doc
D1.excel
任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等
思路：1.先获取文件夹中文件名（os.listdir()）  2.分隔文件名和后缀(os.path.split(path))  3.新建文件夹(os.mkdir(path,[,mode])) 4.移动文件（shutil.move(old,new)）
'''
import  os
#获取文件夹下所有文件
path = 'E:\新建文件夹\zuoye\接口第二天\Data'
s = os.listdir(path)
print(s)
#获取需要构建的文件夹分类
f = []
for i in s:
    a = i.split('.')[1]
    print(a)
    if a  not in f:
        f.append(a)

print(f)
#创建文件类型对应的文件
for j in f:
    os.mkdir(path+'\\'+ j)
#将对应文件移入对应文件夹
for x in range(len(s)):
    if s[x].split('.')[1] in f:
        shutil.move(path+'\\'+s[x],path+'\\'+s[x].split('.')[1])
