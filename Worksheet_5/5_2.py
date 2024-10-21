import numpy as np
from scipy.fftpack import fft2, ifft2

data = np.random.rand(4, 4)
print("Original 2D Array:\n", data)

dft = fft2(data)
print("Discrete Fourier Transform:\n", dft)

inverse_dft = ifft2(dft)
print("Recovered Data from Inverse DFT:\n", inverse_dft.real)