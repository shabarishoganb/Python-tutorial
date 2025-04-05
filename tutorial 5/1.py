import numpy as np

def add_and_transpose(matrix1, matrix2):
    result = np.add(matrix1, matrix2)
    return np.transpose(result)

# Example usage
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(add_and_transpose(A, B))
