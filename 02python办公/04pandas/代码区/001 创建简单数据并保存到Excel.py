import pandas as pd
#创建数据
df = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Victor','Nick']})
# df.dtypes
df = df.set_index('ID')
#保存数据到Excel
print(df)
df.to_excel('D:/Source/Python/02python办公/04pandas/输出数据/001.xlsx')
#提示用户已完成
print('Done!')
