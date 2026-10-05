import numpy as np

matrix1 = np.array([
        [-1, 1],
        [-6, 3]
    ])

matrix2 = np.array([
        [-5, 1],
        [-4, 2]
    ])

matrix3 = np.array([
        [3, 6],
        [1, 6]
    ])


result = matrix1 + matrix2.dot(matrix3)
print(result)