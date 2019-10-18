#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/17 0017 下午 19:52 
# @Author : aiminhu
# @File : lx6-类的继承.py 
# @Software: PyCharm
'''
1.语法--继承谁，类的括号中就写谁
2.继承后，子类就具备父类的所有属性和方法，但是父类不能具备子类的属性和方法
3.如果父类中没有子类需要的方法，可以在子类中自行定义
#注意：实例化和调用方法的时候要区分是否需要传参
'''
class Animal:
    def eat(self):
        print('--------吃')
    def drink(self):
        print('--------喝')

class Dog:
    def eat(self):
        print('--------吃吃')
    def drink(self):
        print('--------喝喝')

class Dog(Animal):
    def bark(self):
        print('---------汪汪叫')


class Cat(Animal):
    def catch(self):
        print('--------抓老鼠')

xiaobai = Dog()
xiaobai.eat()
xiaobai.bark()

'''
练习：
定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
1、实现gh为xx的老师，教xx课
2、实现gh为xx老师，在xx上班，一月工资xx
3、名字是xx，工号为xx的老师，吃饭

'''
class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('%s,吃饭'%self.name)
    def work(self,addr,salary):
        print('在%s上班,一月工资%d'%(addr,salary))
        print('**********')

class Teacher(Person):
    def __init__(self,name,gh):
        self.name = name
        self.gh = gh


    def teach(self,kecheng):
        print('gh为%s的老师，教%s课'%(self.gh,kecheng))
    def work(self,addr,salary):
        print('gh为%s老师,在%s上班,一月工资%d'%(self.gh,addr,salary))
    def eat(self):
        print('名字是%s，工号为%s的老师，吃饭'%(self.name,self.gh))
a = Person('Lily')
a.eat()
a.work('北京',18000)
b = Teacher('Tony','1001')
b.teach('Python')
b.work('beijing',18000)
b.eat()