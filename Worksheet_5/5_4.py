import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = np.cos(x)
f = interpolate.interp1d(x, y, kind='cubic')

x_new = np.linspace(0, 10, 100)
y_new = f(x_new)

plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_new, y_new, '-', label='Interpolated Data')
plt.legend()
plt.show()