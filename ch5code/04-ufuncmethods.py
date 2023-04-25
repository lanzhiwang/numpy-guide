import numpy as np

a = np.arange(9)

print "Reduce", np.add.reduce(a)

# accumulate 方法同样可以递归作用于输入数组。但是与reduce方法不同的是，它将存储运算的中间结果并返回。
# 因此在 add 函数上调用 accumulate 方法，等价于直接调用 cumsum 函数。
print "Accumulate", np.add.accumulate(a)
# [ 0 1 3 6 10 15 21 28 36]

# reduceat 方法需要输入一个数组以及一个索引值列表作为参数
print "Reduceat", np.add.reduceat(a, [0, 5, 2, 7])
# 第一步用到索引值列表中的 0 和 5，实际上就是对数组中索引值在 0 到 5 之间的元素进行 reduce 操作。
#     print "Reduceat step I", np.add.reduce(a[0:5])
#     Reduceat step I 10
# 第二步用到索引值 5 和 2。由于 2 比 5 小，所以直接返回索引值为 5 的元素:
#     print "Reduceat step II", a[5]
#     Reduceat step II 5
# 第三步用到索引值 2 和 7。这一步是对索引值在 2 到 7 之间的数组元素进行 reduce 操作:
#     print "Reduceat step III", np.add.reduce(a[2:7])
#     Reduceat step III 20
# 第四步用到索引值 7。这一步是对索引值从 7 开始直到数组末端的元素进行 reduce 操作:
#     print "Reduceat step IV", np.add.reduce(a[7:])
#     Reduceat step IV 15
# [10 5 20 15]

print "Reduceat step I", np.add.reduce(a[0:5])
print "Reduceat step II", a[5]
print "Reduceat step III", np.add.reduce(a[2:7])
print "Reduceat step IV", np.add.reduce(a[7:])

# outer 方法返回一个数组，它的秩(rank)等于两个输入数组的秩的和。
# 它会作用于两个输入数组之间存在的所有元素对。在 add 函数上调用 outer 方法
print "Outer", np.add.outer(np.arange(3), a)
# [
#     [ 0 1 2 3 4 5 6 7 8]
#     [ 1 2 3 4 5 6 7 8 9]
#     [ 2 3 4 5 6 7 8 9 10]
# ]