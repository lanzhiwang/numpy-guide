import numpy as np
from matplotlib.pyplot import plot, show

# 使用 fft 函数对余弦波信号进行傅里叶变换
# 对变换后的结果应用 ifft 函数，应该可以近似地还原初始信号

x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
transformed = np.fft.fft(wave)
print np.all(np.abs(np.fft.ifft(transformed) - wave) < 10**-9)

plot(transformed)
show()
