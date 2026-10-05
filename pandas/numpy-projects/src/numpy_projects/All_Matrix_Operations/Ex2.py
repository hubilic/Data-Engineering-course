import numpy as np

matrix1 = np.array([
        [2, 6],
        [-6, 4]
    ])

matrix2 = np.array([
        [5, 3],
        [-6, 2]
    ])

matrix3 = np.array([
        [1, 2],
        [2, 0]
    ])

result = np.dot(matrix1, (matrix2 + matrix3))
print(result)
