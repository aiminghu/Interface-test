#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/13 0013 下午 17:18 
# @Author : aiminhu
# @File : lx4.py 
# @Software: PyCharm
'''模块和包'''
def fun1():
    print('fun1')

def fun2():
    print('fun2')
print('mymodule文件的name属性：',__name__)

if __name__ == '__main__':
    fun1()
    fun2()