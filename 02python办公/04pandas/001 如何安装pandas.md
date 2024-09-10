# Pandas教程
**Pandas是Python语言的一个扩展程序，用于数据分析**

Pandas是一个开放源码、BSD 许可的库，提供高性能、易于使用的数据结构和数据分析工具。

Pandas 名字衍生自术语 "panel data"（面板数据）和 "Python data analysis"（Python 数据分析）。

Pandas 一个强大的分析结构化数据的工具集，基础是 Numpy（提供高性能的矩阵运算）。

Pandas 可以从各种文件格式比如 CSV、JSON、SQL、Microsoft Excel 导入数据。

Pandas 可以对各种数据进行运算操作，比如归并、再成形、选择，还有数据清洗和数据加工特征。

Pandas 广泛应用在学术、金融、统计学等各个数据分析领域。
# Pandas安装
安装 pandas 需要基础环境是 Python，开始前我们假定你已经安装了 Python 和 Pip。

使用 pip 安装 pandas:

```text
pip install pandas
```
在python终端中运行下来代码可插件pandas版本
```Python
import pandas as pd
pd.__version__
```
简单生成一个数据表
```Python
mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
```
- [ ] 查看相关教程在[B站](https://www.bilibili.com/video/BV1hk4y1C73S/?spm_id_from=333.337.search-card.all.click&vd_source=1e86fa51619d647790c131281887e3ed)
