import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

coefficients = [3, -5, 2, -8]

roots = np.roots(coefficients)
print(f"Roots of the polynomial: {roots}")

def p(x):
    return 3*x**3 - 5*x**2 + 2*x - 8

x_values = np.linspace(-3, 3, 500)
y_values = p(x_values)
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='p(x) = 3x^3 - 5x^2 + 2x - 8', color='blue')

for root in roots:
    if np.isreal(root):
        plt.scatter(np.real(root), 0, color='red', zorder=5)
        plt.text(np.real(root), 0.5, f'Root: {np.real(root):.2f}', horizontalalignment='center')

plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title("Polynomial p(x) = 3x^3 - 5x^2 + 2x - 8 and its Roots")
plt.xlabel('x')
plt.ylabel('p(x)')
plt.grid(True)
plt.legend()
plt.show()