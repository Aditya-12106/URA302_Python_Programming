import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

years = np.array([2000, 2005, 2010, 2015, 2020])
population = np.array([50, 55, 70, 80, 90])

pearson_corr, _ = stats.pearsonr(years, population)
print(f"Pearson's correlation coefficient: {pearson_corr:.4f}")
slope, intercept, r_value, p_value, std_err = stats.linregress(years, population)
print(f"Linear regression equation: population = {slope:.2f} * year + {intercept:.2f}")

estimated_population_2008 = slope * 2008 + intercept
print(f"Estimated population in 2008: {estimated_population_2008:.2f} thousand")

plt.figure(figsize=(10, 6))
plt.scatter(years, population, color='red', label='Original Data', zorder=5)

years_extended = np.linspace(1995, 2025, 100)
population_fitted = slope * years_extended + intercept
plt.plot(years_extended, population_fitted, label='Linear Regression Line', color='blue')

plt.scatter(2008, estimated_population_2008, color='green', label=f'Estimate for 2008: {estimated_population_2008:.2f}', zorder=6)

plt.title("Population of the Town vs Year with Linear Regression")
plt.xlabel("Year")
plt.ylabel("Population (in thousands)")
plt.legend()
plt.grid(True)
plt.show()