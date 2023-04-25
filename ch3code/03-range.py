import numpy as np

# 1 股票代码:             AAPL,
# 2 dd-mm-yyyy格式的日期: 28-01-2011,
# 3 空:                   ,
# 4 开盘价:               344.17,
# 5 最高价:               344.4,
# 6 最低 9 价:            333.53,
# 7 收盘价:               336.1,
# 8 当日的成交量:          21144800

h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)
print "highest =", np.max(h)
print "lowest =", np.min(l)
print(np.max(h) + np.min(l)) / 2

# NumPy 中有一个 ptp 函数可以计算数组的取值范围。该函数返回的是数组元素的最大值和最小值之间的差值。
# 也就是说，返回值等于 max(array) - min(array)。
print "Spread high price", np.ptp(h)
print "Spread low price", np.ptp(l)
