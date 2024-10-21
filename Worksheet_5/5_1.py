import numpy as np
from scipy import stats

data = np.random.rand(10)
print(f"Array of random numbers {data}")
mean = stats.tmean(data)
median = np.median(data)
variance = stats.tvar(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")