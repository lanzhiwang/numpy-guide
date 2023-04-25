import numpy as np
from datetime import datetime

# 1 股票代码:             AAPL,
# 2 dd-mm-yyyy格式的日期: 28-01-2011,
# 3 空:                   ,
# 4 开盘价:               344.17,
# 5 最高价:               344.4,
# 6 最低 9 价:            333.53,
# 7 收盘价:               336.1,
# 8 当日的成交量:          21144800

# Monday 0
# Tuesday 1
# Wednesday 2
# Thursday 3
# Friday 4
# Saturday 5
# Sunday 6
def datestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()


dates, close = np.loadtxt('data.csv',
                          delimiter=',',
                          usecols=(1, 6),
                          converters={1: datestr2num},
                          unpack=True)
print "Dates =", dates
# Dates = [ 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4. 1. 2. 4. 0. 1. 2. 3. 4. 0. 1. 2. 3. 4.]

averages = np.zeros(5)

# where 函数会根据指定的条件返回所有满足条件的数组元素的索引值。
# take 函数可以按照这些索引值从数组中取出相应的元素。我们将用 take 函数来获取各个工作日的收盘价。
# 在下面的循环体中，我们将遍历 0 到 4 的日期标识，或者说是遍历星期一到星期五，然后用 where 函数得到各工作日的索引值并存储在indices 数组中。在用 take 函数获取这些索引值相应的元素值。
# 最后，我们对每个工作日计算出平均值存放在 averages 数组中。
for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print "Day", i, "prices", prices, "Average", avg
    averages[i] = avg

# argmin 函数返回的是 averages 数组中最小元素的索引值
# argmax 函数返回的是 averages 数组中最大元素的索引值
top = np.max(averages)
print "Highest average", top
print "Top day of the week", np.argmax(averages)

bottom = np.min(averages)
print "Lowest average", bottom
print "Bottom day of the week", np.argmin(averages)
