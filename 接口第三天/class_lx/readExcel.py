#！ /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/28 0028 下午 19:53 
# @Author : aiminhu
# @File : readExcel.py 
# @Software: PyCharm
import xlrd,xlwt,xlutils

'''
xlrd 读excel
xlwt 写excel
'''
#1.打开excel
readbook = xlrd.open_workbook(r'E:\新建文件夹\zuoye\接口第三天\class_lx\\testCase.xlsx')

#2.获取读入的文件的sheet
sheet = readbook.sheet_by_index(0) #索引的方式,从0开始
sheet1 = readbook.sheet_by_name('工作表 1') #通过名字定位sheet页
allsheetnames = readbook.sheet_names() #返回所有sheet页名字组成的列表
# print(allsheetnames)
# 3.获取sheet的最大行数和列数
nrows = sheet.nrows #行
ncols = sheet.ncols #列
# print(nrows,ncols)
# 4.获取某个单元格的值
lng = sheet.cell(0,0).value #获取1行1列的表格值，从0开始
lat = sheet.cell(1,4).value #获取2行5列的表格值，从0开始
# print(lng,lat)
# 5.获取某行、某列的值
row_value = sheet.row_values(4) #获取x行的值，从0开始计数
col_value = sheet.col_values(0) #获取y列的值，从0开始计数
# print(row_value)
# print(col_value)

'''
？？没太懂文件中这个的用处
#使用xlutil.copy 写excel
#1-读取源excel中的所有数据(复制对象)
rb = xlrd.open_workbook(excel_dir + '\\' + 'testCase.xlsx')

#2-f复制读取的源excel对象
wb = copy(rb)

#3-通过get_sheet()获取复制对象的sheet页
ws = wb.get_sheet(0)

#4.对sheet页进行写入（传入x和y坐标，和具体写入的value）
self.ws.write(id,2,real)
self.ws.wirte(id,3,status)

#5-保存excel(具体的excel路径+名称)
self.wb.save(self.excel_dir + '\\'+'testCase.xlsx')
'''


