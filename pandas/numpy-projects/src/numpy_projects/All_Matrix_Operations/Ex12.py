import numpy as np

matrix1 = np.array([
        [-5, 1],
        [-4, -5]
])

matrix2 = np.array([
        [5, -4, 2],
        [-6, 3, -6]
])

matrix3 = np.array([
        [3, -5, 2], 
        [5, 5, 3]
])

result = matrix1.dot(matrix2 + matrix3)
print(result)