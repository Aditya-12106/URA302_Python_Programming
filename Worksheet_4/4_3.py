import numpy as np

#Part 1
array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([1, 3, 5, 7, 9])
print("Array 1:", array1)
print("Array 2:", array2)

#Part 2
print("\nAddition:", array1+array2)
print("Subtraction:", array1-array2)
print("Element-wise multiplication:", array1*array2)
print("Element-wise division:", np.round(array1 / array2, 2))