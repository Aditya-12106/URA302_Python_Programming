import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import minimize_scalar

def f(x):
    return x**4 - 3*x**3 + 2
result = minimize_scalar(f, bounds=(-2, 3), method='bounded')
local_min_x = result.x
local_min_y = result.fun
print(f"Local minima at x = {local_min_x:.4f}, f(x) = {local_min_y:.4f}")

x_values = np.linspace(-2, 3, 500)
y_values = f(x_values)
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$f(x) = x^4 - 3x^3 + 2$', color='blue')
plt.scatter(local_min_x, local_min_y, color='red', zorder=5, label=f'Local minima at x = {local_min_x:.4f}')

plt.title(r"Plot of $f(x) = x^4 - 3x^3 + 2$ with Local Minima")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.grid(True)
plt.show()