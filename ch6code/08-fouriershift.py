import numpy as np
from matplotlib.pyplot import plot, show

# numpy.linalg 模块中的 fftshift 函数可以将 FFT 输出中的直流分量移动到频谱的中央
# ifftshift 函数则是其逆操作

x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
transformed = np.fft.fft(wave)
shifted = np.fft.fftshift(transformed)
print np.all(np.abs(np.fft.ifftshift(shifted) - transformed) < 10**-9)

plot(transformed, lw=2)
plot(shifted, lw=3)
show()
