import numpy as np
from scipy import linalg

matrix = np.array([[4, 2, 1],
                   [2, 5, 3],
                   [1, 3, 6]])

determinant = linalg.det(matrix)
inverse = linalg.inv(matrix)
eigenvalues, eigenvectors = linalg.eig(matrix)

print(f"Determinant: {determinant}")
print(f"Inverse:\n{inverse}")
print(f"Eigenvalues: {eigenvalues}")