import numpy as np

# Create two matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)

# Element-wise operations
elementwise_sum = matrix_a + matrix_b
elementwise_product = matrix_a * matrix_b

print("Matrix A:")
print(matrix_a)

print("Matrix B:")
print(matrix_b)

print("Matrix Product:")
print(matrix_product)

print("Element-wise Sum:")
print(elementwise_sum)

print("Element-wise Product:")
print(elementwise_product)