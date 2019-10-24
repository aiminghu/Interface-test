#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/18 0018 下午 12:34 
# @Author : aiminhu
# @File : lx8-类的多态.py 
# @Software: PyCharm
'''
多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数
参数类型用基类声明，执行的时候会根据传入的对象（同名方法）去执行相应的方法，具有不同的效果
即同一个函数，传不同的类（父类、子类）
关键在于：同样调用相同的方法，但是完成的内容不同
'''
class Dog:
    def print_self(self):
        print("大家好，我是XXXX")

class Xiaotq(Dog):
    def print_self(self):
        print("Hello,everybody,我是哮天犬")

def introduce(temp):
    #需要接收一个Dog的类型或者其子类的类型
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)

'''
私有属性和私有方法
类的私有属性
__abc：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__abc。
类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
类的私有方法
__method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__ methods。

'''
#如果调用的是继承父类中的公有方法可以在这个公有方法中访问父类中的私有属性和私有方法
#但是如果在子类中实现了一个公有方法，那么这个方法是不能够调用继承父类中的私有方法和属性的

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
        # print(self.num1,self.__num2)

    def test1(self):
        print("----公有方法")

    def __test2(self):
        print("-----私有方法")

    def test3(self):
        print("----公有方法中调用私有方法和私有属性")
        self.__test2()
        print(self.num1)
        print(self.__num2)

class B(A):
    def test4(self):
        self.__test2()

a = A()
a.test3()

b = B()
# b.test4() #会报错AttributeError: 'B' object has no attribute '_B__test2'
