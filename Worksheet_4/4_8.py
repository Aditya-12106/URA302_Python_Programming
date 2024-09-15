import numpy as np

#Part 1
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", matrix_A)
print("\nMatrix B:\n", matrix_B)

#Part 2
matrix_multiplication = np.dot(matrix_A, matrix_B)
transpose_A = np.transpose(matrix_A)
print("\nMatrix multiplication (A * B):\n", matrix_multiplication)
print("\nTranspose of Matrix A:\n", transpose_A)