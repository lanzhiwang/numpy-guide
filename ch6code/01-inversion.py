import numpy as np

# 矩阵 A 与其逆矩阵相乘后会得到一个单位矩阵 I。numpy.linalg 模块中的 inv 函数可以计算逆矩阵

A = np.mat("0 1 2;1 0 3;4 -3 8")
print "A\n", A

inverse = np.linalg.inv(A)
print "inverse of A\n", inverse

print "Check\n", A * inverse
