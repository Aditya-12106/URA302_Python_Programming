import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])

def quadratic_func(t, a, b, c):
    return a * t**2 + b * t + c

params, covariance = curve_fit(quadratic_func, time, velocity)

a, b, c = params
print(f"Fitted parameters: a = {a}, b = {b}, c = {c}")

fitted_velocity = quadratic_func(time, a, b, c)

time_fine = np.linspace(0, 5, 100)
fitted_curve = quadratic_func (time_fine, a, b, c)

plt.figure(figsize=(10, 6))

plt.scatter(time, velocity, color='red', label='Original Data', zorder=5)

plt.plot(time_fine, fitted_curve, label=f'Fitted Curve: $v(t) = {a:.2f}t^2 + {b:.2f}t + {c:.2f}$', color='blue')

plt.title('Velocity vs Time with Curve Fitting')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.grid(True)
plt.show()