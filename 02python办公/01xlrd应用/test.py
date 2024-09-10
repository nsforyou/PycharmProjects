'''
https://www.bilibili.com/video/BV1JT411w7Ea?p=2&vd_source=1e86fa51619d647790c131281887e3ed
在终端中输入下列代码以安装xlrd模块
pip install xlrd
由于xlrd升级后不支持xlsx文件读取,只能通过降版本的形式解决问题
查看xlrd模块版本
pip list
卸载高版本
pip uninstall xlrd
安装指定版本
pip install xlrd==1.2.0
'''
# 调用xlrd模块
import xlrd
# 打开Excel Python\02pythonExcel\01xlrd应用\test.xlsx
# 因为\是转义符,所以在相对路径前加r
wb = xlrd.open_workbook(r'Python\02pythonExcel\01xlrd应用\test.xlsx')
print(f'excel中有{wb.nsheets}个工作簿')
print(f'excel中工作簿的名字分别为{wb.sheet_names()}')
# 选择工作表
sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_name('电影')
#print(sh1)
#print(sh2)
#查看有数据的范围
print(f'sheet里面一共有{sh1.nrows}行{sh2.ncols}列的数据')
# 获取单元格的值
# 三种获取单元格值的方法
print(f'第一行第二列的值:{sh1.cell_value(0,1)}')
print(f'第一行第二列的值:{sh1.cell(0,1).value}')
print(f'第一行第二列的值:{sh1.row(0)[1].value}')
#获取整行数据
print(sh1.row_values(0))
#获取整列数据
print(sh1.col_values(0))
#遍历所有数据
for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'第{r}行 第{c}列的数据是{sh1.cell_value(r,c)}')