import numpy as np


def ultimate_answer(a):
    # zeros_like 函数创建一个和 a 形状相同，并且元素全部为 0 的数组 result
    result = np.zeros_like(a)
    # flat 属性为我们提供了一个扁平迭代器，可以逐个设置数组元素的值
    result.flat = 42

    return result

# 使用 frompyfunc 创建通用函数。指定输入参数的个数为 1，随后的 1 为输出参数的个数
ufunc = np.frompyfunc(ultimate_answer, 1, 1)
print "The answer", ufunc(np.arange(4))
# [42 42 42 42]

print "The answer", ufunc(np.arange(4).reshape(2, 2))
