import numpy as np

# 使用 numpy.linalg 模块中的 pinv 函数计算了矩阵的广义逆矩阵

A = np.mat("4 11 14;8 7 -2")
print "A\n", A

pseudoinv = np.linalg.pinv(A)
print "Pseudo inverse\n", pseudoinv

print "Check", A * pseudoinv
