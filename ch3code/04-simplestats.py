import numpy as np

# 1 股票代码:             AAPL,
# 2 dd-mm-yyyy格式的日期: 28-01-2011,
# 3 空:                   ,
# 4 开盘价:               344.17,
# 5 最高价:               344.4,
# 6 最低 9 价:            333.53,
# 7 收盘价:               336.1,
# 8 当日的成交量:          21144800

c = np.loadtxt('data.csv', delimiter=',', usecols=(6, ), unpack=True)
# median 函数将帮助我们找到中位数
print "median =", np.median(c)

# msort 排序数组
sorted = np.msort(c)
print "sorted =", sorted

N = len(c)
print "middle =", sorted[(N - 1) / 2]
print "average middle =", (sorted[N / 2] + sorted[(N - 1) / 2]) / 2

# 方差
# 方差是指各个数据与所有数据算术平均数的离差平方和除以数据个数所得到的值。
print "variance =", np.var(c)
print "variance from definition =", np.mean((c - c.mean())**2)
