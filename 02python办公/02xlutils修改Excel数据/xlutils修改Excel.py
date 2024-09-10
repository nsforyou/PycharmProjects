'''
在终端中输入代码安装模块 pip install xlutils
被改写过的Excel文件需要变更后缀为xls才能用Excel正常打开
'''
import xlrd
from xlutils.copy import copy
#打开Excel
read_book = xlrd.open_workbook(r'Python\02pythonExcel\02xlutils修改Excel数据\test.xls')
#复制数据
wb = copy(read_book)
# 选择工作表
sh = wb.get_sheet(0)
#添加数据
sh.write(5,0,'保家卫国')
sh.write(5,1,133)
sh.write(5,2,5.1)
sh.write(5,3,490)
#增加工作表
sh2 = wb.add_sheet('数据汇总')
#汇总票房数据
count = 0
rs = read_book.sheet_by_index(0)
for i in range(1,rs.nrows):
    num = rs.cell_value(i,3)
    count += num
#数据写在新工作表中
sh2.write(0,0,'总票房')
sh2.write(0,1,count)
wb.save(r'Python\02pythonExcel\02xlutils修改Excel数据\test_修改.xls')