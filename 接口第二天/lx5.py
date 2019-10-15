#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/13 0013 下午 17:37 
# @Author : aiminhu
# @File : lx5.py 
# @Software: PyCharm
'''类和对象'''

class Person():

    #构造方法，在实例化的时候自动被执行,且必须要传写入的参数;实例化里的属性必须要加self
    def __init__(self,name,sex):
        print('执行init方法')
        self.name = name
        self.sex = sex


    # 属性
    #类方法
    def eat(self,food):
        print('吃',food)

    def sleep(self):
        print(self.name,'睡觉')

#实例化
a = Person('小明','男')
#调用类中的方法
a.sleep()
# a.eat('酸辣粉')

class Student():

    def __init__(self,name,kecheng,sno):
        print('执行init方法')
        self.name = name
        self.kecheng = kecheng
        self.sno = sno

    def study(self):
        print(self.name,'学习',self.kecheng)
    def study_1(self):
        print('学号为'+self.sno+'的学生，学习'+self.kecheng)
b = Student('白雪','Python','10010')
b.study()
b.study_1()
