import numpy as np

matrix1 = np.array([
        [-1, 5],
        [5, -5]
    ])

matrix2 = np.array([
        [-3, 6],
        [-3, 0]
    ])

result = np.dot(matrix1, matrix2)
print(result)
