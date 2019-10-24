#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/13 0013 下午 16:44 
# @Author : aiminhu
# @File : lx3.py 
# @Software: PyCharm
'''列表推导式[循环体 循环结构 循环条件]'''
# a = [i for i in range(1,5)]
# print([i for i in range(1,5) if i%2 == 0])
# print(a)

'''
字符串的相关方法
'''
s = 'hello world'
print(s.split('l'))
print(s.swapcase())

a = [1,2,3,4]
a1 = [str(i) for i in a]
print('+'.join(a1))

