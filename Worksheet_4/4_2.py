import numpy as np

array_1d = np.arange(5, 26)
array_2d = np.random.randint(10, 51, size=(3, 4))

#Part 1
print("1D array:")
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Data type:", array_1d.dtype)

#Part 2
print("\n2D array:")
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Data type:", array_2d.dtype)
