#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/10 0010 上午 11:47 
# @Author : aiminhu
# @File : test_myfun.py 
# @Software: PyCharm
import unittest
import os
import HTMLTestRunner
from  接口第五天.myfun import *

'''
坑1：集成unittest.TestCase类时，光标最好放到main函数执行
坑2：pycharm设置问题 https://www.cnblogs.com/kaerxifa/p/11046156.html
'''
class TestMyFun(unittest.TestCase):
    # TestCase基类方法，所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法，所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作")

    #Testcase基类方法，每次执行case前自动执行
    def setUp(self):
        print("***这里是一个测试用例前的准备工作***")


    #Testcase基类方法，每次执行case后自动执行
    def tearDown(self):
        print("***这里是一个测试用例后的清理工作***")

    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2)) #测试业务方法add
        print('this is add')

    def test_minus(self):
        self.assertEqual(1,minus(3,2)) #测试业务方法minus
        print('this is minus')

    def test_multi(self):
        self.assertEqual(6,multi(2,3)) #测试业务方法multi
        print('this is multi')

    def test_divide(self):
        self.assertEqual(2,divide(6,3)) #测试业务方法divide
        print('this is divide')


if __name__ == '__main__':
    #默认全部运行

    #生成测试报告
    suite = unittest.TestSuite()

    suite.addTest(TestMyFun('test_add'))

    filename = r'E:\新建文件夹\zuoye\接口第五天\result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告头部',description=u'用例执行情况')
    # 4. 运行测试用例
    runner.run(suite)
    # 5.关闭报告文件
    fp.close()
