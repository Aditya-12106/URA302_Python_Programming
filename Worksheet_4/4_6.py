import numpy as np

#Part 1
array_1d = np.random.randint(20, 41, size=10)
print("Original array:", array_1d)

#Part 2
greater_than_30 = array_1d[array_1d > 30]
print("\nElements greater than 30:", greater_than_30)