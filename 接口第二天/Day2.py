#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/18 0018 下午 14:31 
# @Author : aiminhu
# @File : Day2.py 
# @Software: PyCharm

#打印小猫爱吃鱼，小猫爱喝水

class Cat():
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('%s爱吃%s'%(self.name,food))

    def drink(self,drink):
        print('%s要喝%s'%(self.name,drink))

a = Cat('小猫')
a.eat('鱼')
a.drink('水')

# 2、小明爱跑步，爱吃东西。
#     1）小明体重75.0公斤
#     4）小美的体重是45.0公斤
#     2）每次跑步会减肥0.5公斤
#     3）每次吃东西体重会增加1公斤
#
class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def p_weight(self):
        print('%s体重是%.2f公斤'%(self.name,self.weight))

    def run(self):
        self.weight = self.weight - 0.5
        print('%s跑步一次，此时的体重为%.2f'%(self.name,self.weight))

    def eat(self):
        self.weight = self.weight + 1
        print('%s吃东西一次，此时的体重为%.2f'%(self.name,self.weight))

p = Person('小明',75.0)
p.p_weight()
p.run()
p.eat()
P1 = Person('小红',45.0)
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name,self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        #剩余面积
        self.free_area = area

        #家具名称列表
        self.item_list = []

    def __str__(self):
        #Python 能够自动的将一对括号内部的代码连接在一起
        return ("该房子的户型：%s；总面积：%.2f；[剩余：%2.f]；家具：%s"
                %(self.house_type,self.area,
                  self.free_area,self.item_list))

    def add_item(self,item):
        print("要添加 %s" % item)
        #1.判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)

            return

        #2.将家具的名称添加到列表中
        self.item_list.append(item.name)

        #3.计算剩余面积
        self.free_area -= item.area

#1.创建家具
bed = HouseItem("床",40)
chest =HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)
print(bed)
print(chest)
print(table)

#2.创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)

# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None  #####这里先设为None  等枪示例化后再给
        print('****************8')
    def __str__(self):
        return '士兵%s有一把%s,%s。' % (self.name, self.gun.model, self.gun)
        # 这里gun.model为枪名字 gun为gun类的str

    def fire(self):
        if self.gun == None:
            print("没有武器！")
            return False
        self.gun.add_bullet(10)
        self.gun.shoot()
        return True

class gun:
    def __init__(self, model, bullet_count=0):
        self.model = model
        self.bullet_count = bullet_count

    def __str__(self):
        return '这把%s剩余%d子弹' % (self.model, self.bullet_count)

    def shoot(self):
        if self.bullet_count == 0:
            return False
        self.bullet_count -= 1
        print('发射一颗子弹')
        return True

    def add_bullet(self, count):
        self.bullet_count += count
        print('填充%d颗子弹' % count)
        return True

B = gun('AK-47')  # 填充30颗子弹
B.add_bullet(30)  # 发射一颗子弹
B.shoot()  # 射击
A = Soldier('瑞恩')  # 发射一颗子弹
A.gun = B  # 将实例化的枪给士兵
A.fire()  # 士兵开火
print(A)  ##士兵瑞恩有一把AK-47,这把AK-47剩余38子弹





