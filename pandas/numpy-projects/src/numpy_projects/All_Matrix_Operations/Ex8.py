import numpy as np

matrix1 = np.array([
        [2], 
        [-1],
        [-6]
    ])

matrix2 = np.array([
        [2], 
        [-4],
        [4]
    ])

result = -5 * (matrix1 + matrix2)
print(result)