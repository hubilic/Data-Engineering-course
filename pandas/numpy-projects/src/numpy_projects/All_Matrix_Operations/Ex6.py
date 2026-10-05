import numpy as np

matrix1 = np.array([
        [-3, -6], 
        [1, 4]
    ])
matrix2 = np.array([
        [-2, 6], 
        [-1, -4]
    ])


result = -4 * (matrix1.dot(matrix2))
print(result)