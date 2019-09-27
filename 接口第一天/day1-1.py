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



if __name__ == '__main__':
    # sortSore()
    # readList()
    get_factorial(1)