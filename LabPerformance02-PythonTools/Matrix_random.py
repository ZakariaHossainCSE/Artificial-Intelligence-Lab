import numpy as np
matrix = np.random.randint(0, 100, size=(5, 5))
row_sums = np.sum(matrix, axis=1)
print("Matrix:")
print(matrix)
print("\nRow-wise sums:")
print(row_sums)
