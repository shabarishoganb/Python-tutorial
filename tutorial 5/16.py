import numpy as np

# Create two random 3x3 matrices
A = np.random.randint(0, 20, (3, 3))
B = np.random.randint(0, 20, (3, 3))

# Perform matrix addition
addition = A + B

# Perform matrix multiplication
multiplication = np.dot(A, B)

# Compute transpose of the product matrix
transpose_product = multiplication.T

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Addition:\n", addition)
print("Multiplication:\n", multiplication)
print("Transpose of Product:\n", transpose_product)
