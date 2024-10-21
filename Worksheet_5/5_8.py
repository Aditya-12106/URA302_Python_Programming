import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])

def quadratic_model(t, a, b, c):
    return a * t**2 + b * t + c

params, _ = curve_fit(quadratic_model, time, velocity)

a, b, c = params

print(f"Fitted coefficients: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")

fitted_velocity = quadratic_model(time, a, b, c)

plt.scatter(time, velocity, color='red', label='Data (Time vs Velocity)')
plt.plot(time, fitted_velocity, label=f'Fitted Model: {a:.4f}t^2 + {b:.4f}t + {c:.4f}', color='blue')
plt.xlabel('Time (Seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Curve Fitting for Velocity over Time')
plt.legend()
plt.show()