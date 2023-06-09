from __future__ import division
import numpy as np

a = np.array([2, 6, 5])
b = np.array([1, 2, 3])

# divide 函数在整数和浮点数除法中均只保留整数部分
print "Divide", np.divide(a, b), np.divide(b, a)

# true_divide 函数与数学中的除法定义更为接近，即返回除法的浮点数结果而不作截断
print "True Divide", np.true_divide(a, b), np.true_divide(b, a)

# floor_divide 函数总是返回整数结果，相当于先调用 divide 函数再调用 floor 函数。
# floor 函数将对浮点数进行向下取整并返回整数
print "Floor Divide", np.floor_divide(a, b), np.floor_divide(b, a)
c = 3.14 * b
print "Floor Divide 2", np.floor_divide(c, b), np.floor_divide(b, c)

# 使用 / 运算符相当于调用 divide 函数
print "/ operator", a / b, b / a

# 运算符 // 对应于 floor_divide 函数
print "// operator", a // b, b // a
print "// operator 2", c // b, b // c
