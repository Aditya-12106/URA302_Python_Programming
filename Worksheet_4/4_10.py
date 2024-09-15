import numpy as np

#Part 1
matrix_A = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print("Matrix A:\n", matrix_A)

#Part 2
determinant_A = np.linalg.det(matrix_A)
print("\nDeterminant of matrix A:", determinant_A)

try:
    inverse_A = np.linalg.inv(matrix_A)
except np.linalg.LinAlgError:
    inverse_A = "Matrix is singular and cannot be inverted"
print("\nInverse of matrix A:\n", inverse_A)

eigenvalues, eigenvectors = np.linalg.eig(matrix_A)
print("\nEigenvalues of matrix A:", eigenvalues)
print("\nEigenvectors of matrix A:\n", eigenvectors)