import numpy as np

#Part 1
array_1d = np.arange(11, 23)
print("1D Array with 12 elements startng from 11:")
print(array_1d)

#Part 2
array_2d = array_1d.reshape(3, 4)
print("\nReshaped 2D array:\n", array_2d)