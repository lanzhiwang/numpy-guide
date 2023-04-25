import numpy as np

# 1 股票代码:             AAPL,
# 2 dd-mm-yyyy格式的日期: 28-01-2011,
# 3 空:                   ,
# 4 开盘价:               344.17,
# 5 最高价:               344.4,
# 6 最低 9 价:            333.53,
# 7 收盘价:               336.1,
# 8 当日的成交量:          21144800

# 数据存储在 data.csv 文件中，我们设置分隔符为,(英文标点逗号)，因为我们要处理一个 CSV 文件。
# usecols 的参数为一个元组，以获取第 7 字段至第 8 字段的数据，也就是股票的收盘价和成交量数据。
# unpack 参数设置为 True，意思是分拆存储不同列的数据，即分别将收盘价和成交量的数组赋值给变量 c 和 v。
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)

# VWAP(Volume-Weighted Average Price，成交量加权平均价格)是一个非常重要的经济学量，它代表着金融资产的“平均”价格。
# 某个价格的成交量越高，该价格所占的权重就越大。VWAP 就是以成交量为权重计算出来的加权平均值，常用于算法交易。
vwap = np.average(c, weights=v)
print "VWAP =", vwap

# 算术平均值函数，这个函数可以计算数组元素的算术平均值。
print "mean =", np.mean(c)

# 在经济学中，TWAP(Time-Weighted Average Price，时间加权平均价格)是另一种“平均” 价格的指标。
# 既然我们已经计算了VWAP，那也来计算一下TWAP吧。
# 其实TWAP只是一个变种而已，基本的思想就是最近的价格重要性大一些，所以我们应该对近期的价格给以较高的权重。
# 最简单的方法就是用 arange 函数创建一个从 0 开始依次增长的自然数序列，自然数的个数即为收盘价的个数。
# 当然，这并不一定是正确的计算TWAP的方式。事实上，本书中关于股价分析的大 部分示例都仅仅是为了说明问题。计算TWAP的代码如下。
t = np.arange(len(c))
print "twap =", np.average(c, weights=t)
