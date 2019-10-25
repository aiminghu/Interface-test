#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/13 0013 上午 10:46 
# @Author : aiminhu
# @File : class_lx.py
# @Software: PyCharm
#循环
#循环四要素：
#1、定义循环变量 2、循环条件 3、循环体  4、荀焕边发生变化

#先写循环体，然后1/2/4
def wp(n):
    '''while循环计算1+2+3+...100的值'''
    i = 0
    sum = 0
    while i<n:
        sum += i
        i += 1
    print('最后的和为',sum)

def fp():
    '''for循环： range()'''
    for i in [1,2,4,1]:
        print(i,'ok')

def pthree():
    n = 1
    l = []
    for n in range(1, 100):
        if n % 3 == 0:
            l.append(n)
            # n += 1
    print(l)


def jxq(a,b):
    '''位置参数实例，加减乘除'''
    # a,b = int(input('请输入你要计算的两个数'))
    c = input('请输入你要选择的运算方式：')
    if c == '*':
        return a * b
    if c == '/':
        try:
            return  a/b
        except BaseException as msg:
            return msg
        finally: #优先级高，会覆盖前一个return
            return '程序执行完毕！'
        # if b == 0:
        #     return '被除数不能为0'
        # else:
        #     return a / b

    if c == '-':
        return a - b
    if c == '+':
        return a + b
    else:
        return '你输入的运算方式有问题，请输入=,-,*/其中一种'
        # jxq(a, b)


def jxq_a(a, b):
    '''位置参数实例，加减乘除'''
    # a,b = int(input('请输入你要计算的两个数'))
    c = input('请输入你要选择的运算方式：')
    try:
        if c == '*':
            return a * b
        if c == '/':
            try:
                return a / b
            except BaseException as msg:
                return msg
            # if b == 0:
            #     return '被除数不能为0'
            # else:
            #     return a / b

        if c == '-':
            return a - b
        if c == '+':
            return a + b
    except BaseException as msg:
        return '有问题'
    finally:
        return '程序执行完毕！'


def add_end(L=[]):#列表是可变对象，会记录上次的结果
    print(L)
    L.append('End')
    return L

def add_end_a(L=None):#解决方法:指向不变对象
    # print(L)
    if L is None:
        L = []
    L.append('End')
    return L

def calc(*numbers):
    '''可变参数实例'''
    print(*numbers)
    print(numbers)
    sum = 1
    for n in numbers:
        sum *= n
    return sum

def person(name,age,**kwargs):
    '''可变参数实例'''
    print('name',name,'age',age,kwargs)

def clac_a(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('除数不能为0')

def clac_b(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        '''系统给的异常信息'''
        print(msg)

def clac_c(a,b):
    try:
        print(a/b)
    except BaseException:
        '''异常基类'''
        print('除数不能为0')

if __name__ == '__main__':
    # wp(101)
    # fp()
    # pthree()
    # print(jxq(1,0))
    # print(add_end_a())
    # print(add_end_a())
    # num = [1,2,4]
    # num1 = [1,2,3,4,5]
    # print(calc(7,*num,*num1))
    # # print(calc(num))
    # args = {'city':'Beijing','sex':'性别'}
    # person('xiaohong',18,**args)
    # a = int(input('-'))
    # b = int(input('-'))
    # clac_b(1,0)
    print(jxq(1,0))