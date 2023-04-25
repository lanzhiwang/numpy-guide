import numpy as np

a = np.arange(-4, 4)


# remainder 函数逐个返回两个数组中元素相除后的余数。如果第二个数字为0，则直接返回 0
print "Remainder", np.remainder(a, 2)

# mod 函数与 remainder 函数的功能完全一致
print "Mod", np.mod(a, 2)

# % 操作符仅仅是 remainder 函数的简写
print "% operator", a % 2

# fmod 函数处理负数的方式与 remainder、mod 和 % 不同。所得余数的正负由被除数决定，与除数的正负无关
print "Fmod", np.fmod(a, 2)
