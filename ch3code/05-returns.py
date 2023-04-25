import numpy as np

# 1 股票代码:             AAPL,
# 2 dd-mm-yyyy格式的日期: 28-01-2011,
# 3 空:                   ,
# 4 开盘价:               344.17,
# 5 最高价:               344.4,
# 6 最低 9 价:            333.53,
# 7 收盘价:               336.1,
# 8 当日的成交量:          21144800

# 简单收益率是指相邻两个价格之间的变化率
# 对数收益率是指所有价格取对数后两两之间的差值

c = np.loadtxt('data.csv', delimiter=',', usecols=(6, ), unpack=True)

# NumPy 中的 diff 函数可以返回一个由相邻数组元素的差值构成的数组
# 简单收益率
returns = np.diff(c) / c[:-1]
# 收益率的标准差
print "Standard deviation =", np.std(returns)

# 对数收益率
logreturns = np.diff(np.log(c))

# where 函数可以根据指定的条件返回所有满足条件的数组元素的索引值
posretindices = np.where(returns > 0)
print "Indices with positive returns", posretindices

# 在投资学中，波动率(volatility)是对价格变动的一种度量。
# 历史波动率可以根据历史价格数据计算得出。
# 计算历史波动率(如年波动率或月波动率)时，需要用到对数收益率。年波动率等于对数收益率的标准差除以其均值，
# 再除以交易日倒数的平方根，通常交易日取 252 天。我们用 std 和 mean 函数来计算
annual_volatility = np.std(logreturns) / np.mean(logreturns)
# sqrt 平方根
annual_volatility = annual_volatility / np.sqrt(1. / 252.)
print "Annual volatility", annual_volatility

print "Monthly volatility", annual_volatility * np.sqrt(1. / 12.)
