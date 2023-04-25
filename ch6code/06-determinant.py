import numpy as np

# 使用 numpy.linalg 模块中的 det 函数计算了矩阵的行列式

A = np.mat("3 4;5 6")
print "A\n", A

print "Determinant", np.linalg.det(A)
