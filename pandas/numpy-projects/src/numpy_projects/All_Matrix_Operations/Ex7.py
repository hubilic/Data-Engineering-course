import numpy as np

matrix1 = np.array([
    [3, 1, 3],
    [0, 5, -3]
])

matrix2 = np.array([
    [-1, 3],
    [6, 1]
])

matrix3 = np.array([
    [0, -6, -1],
    [1, 1, 4]
])

result = matrix1 + matrix2.dot(matrix3)
print(result)