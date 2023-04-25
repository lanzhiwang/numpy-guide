import numpy as np

# 在创建矩阵的专用字符串中，矩阵的行与行之间用分号隔开，行内的元素之间用空格隔开。
A = np.mat('1 2 3; 4 5 6; 7 8 9')
print "Creation from string", A

# 用 T 属性获取转置矩阵
print "transpose A", A.T

# 用 I 属性获取逆矩阵
print "Inverse A", A.I
print "Check Inverse", A * A.I

# 使用 NumPy 数组创建矩阵
print "Creation from array", np.mat(np.arange(9).reshape(3, 3))
