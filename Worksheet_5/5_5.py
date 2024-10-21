import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
data = np.sin(2 * np.pi * 50 * t) + 0.5 * np.random.randn(t.size)

b, a = signal.butter(4, 0.1)
filtered_data = signal.filtfilt(b, a, data)

plt.plot(t, data, label='Noisy Data')
plt.plot(t, filtered_data, label='Filtered Data')
plt.legend()
plt.show()