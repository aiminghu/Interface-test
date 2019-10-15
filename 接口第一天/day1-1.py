#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/26 0026 下午 16:19 
# @Author : aiminhu
# @File : day1-1.py 
# @Software: PyCharm


#练习1：输入一个数，判断其等级。90-100为A,--60为E
def sortSore():

    try:
        num = int(input("请输入一个数字："))  # 需要强制转化成数字，不然不能进行比较
        if num > 100:
            print("你的等级是S")
        elif 90 <= num < 100:
            print("你的等级是A")
        elif 80 <= num < 90:
            print("你的等级是B")
        elif 70 <= num < 80:
            print("你的等级是C")
        elif 60 <= num < 70:
            print("你的等级是E")
        else:
            print("你的等级是F")
    except:
        print("你输入的不是一个数字")

#定义一个列表，从键盘中输入一个随机数，判断该数是不是在列表中
def readList():
    lists = ["a",23,34,56,667,'b','c']
    li = input("从键盘上输入一个随机数：")
    try:
        a = int(li)
        if a in lists:
            print("在列表中")
    except:
        if li in lists:
            print("在列表中")
        else:
            print("不在列表中")

#求10的阶乘  阶乘的公式：n! =1*2*3*..n   or n! =n*(n-1)!
def get_factorial(num):
    fac = 1
    if num <0:
        print("负数没有阶乘")
    elif num == 0:
        print("0的阶乘等于1")
    else:
     for i in range(1,num+1):
         fac = fac*i
     print("%d 的阶乘为 %d" % (num, fac))

#求100以内能被3整除的数，并将作为列表输出
#思路：1,定义一个空列表 2，循环添加被3整除的数 3，输出
def get_three():
    li = []
    for i in range(1,101):
        if i%3 == 0:
            li.append(i)
    print(li)

#将列表去重[1,2,3,4,3,4,2,5,5,8,9,7]
#思路1，新建一个列表，循环遍历，不在新列表里就添加进去 2,输出
def del_duplicate():
    a = [1,2,3,4,3,4,2,5,5,8,9,7]
    b = []
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
    print(b)

#求斐波那契数列 1 1 2 3 5 8 13
#思路：n=1,[1] n=2,[1,1]  n=3 [1,1,1+1]

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

#求10000以内的质数  质数：大于1的自然数，除了1和它本身不能被任何数整除
#思路 能被2
def zs():
    num = []
    i = 2
    for i in range(2, 10000):
        j = 2
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            num.append(i)
    print(num)
def zs_1():
    L1 = range(1,101)
    m = 2

if __name__ == '__main__':
    # sortSore()
    # readList()
    # get_factorial(1)
    # get_three()
    # del_duplicate()
    # print(fib(50))
    zs()