#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/18 0018 上午 10:07 
# @Author : aiminhu
# @File : lx7-类的重写.py 
# @Software: PyCharm
'''
当继承的父类方法不满足自身需要的时候，我们可以重写该父类方法。
注意：必须要同名
调用父类的方法：1.调用被重写的方法，父类的名字.方法名()  2.super().方法名()

'''
#eg:
class Animal:
    def eat(self):
        print('------吃')

    def drink(self):
        print('------喝')

class Dog(Animal):
    def bark(self):
        print('------汪汪叫')

class Xiaotq(Dog):
    def fly(self):
        print('***飞')

    def bark(self):
        print('***哮天犬长啸')
        #第一种调用被重写的方法，父类的名字.方法名()
        Dog.bark(self)
        #第二种
        super().bark()

x = Xiaotq()
x.fly()
x.bark()
#子类可以拥有父类的父类的功能
x.eat()

#多重继承注意事项：1.方法的查找顺序是按照继承的最近原则，先查找自身，在查找
class Base(object):
    def test(self):
        print('#####base')

class A(Base):
    def test1(self):
        print('#######test1')

class B(Base):
    def test2(self):
        print('-----test2')

class C(A,B):
    pass

c = C()
c.test()
c.test1()
c.test2()