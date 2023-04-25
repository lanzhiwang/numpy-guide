import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys

# 使用 linspace 函数初始化变量 t，即从 -pi 到 pi 上均匀分布的 201 个点

a = float(sys.argv[1])
b = float(sys.argv[2])
t = np.linspace(-np.pi, np.pi, 201)
x = np.sin(a * t + np.pi / 2)
y = np.sin(b * t)
plot(x, y)
show()
