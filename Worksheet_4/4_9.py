import numpy as np

#Part 1
array_1d = np.random.randint(10, 61, size=15)
print("Array:", array_1d)

#Part 2
print("\nMean:", np.mean(array_1d))
print("\nMedian:", np.median(array_1d))
print("\nStandard Deviation:", np.std(array_1d))