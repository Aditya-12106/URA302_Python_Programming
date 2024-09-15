import numpy as np

#Part 1
array_2d = np.arange(10, 26).reshape(4, 4)
print("Original 2D array with values from 10 to 25:\n", np.arange(10, 26).reshape(4, 4))

#Part 2
second_row = array_2d[1]
last_column = array_2d[:, -1]
print("\nSecond row:\n", second_row)
print("\nLast column:\n", last_column)

#Part 3
array_2d[0] = 0
print("\nArray after replacing the first row with zeros:\n", array_2d)