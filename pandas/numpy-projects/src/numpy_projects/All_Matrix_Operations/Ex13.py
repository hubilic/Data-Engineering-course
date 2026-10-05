import sympy as sp

x, y = sp.symbols("x y")

matrix1 = sp.Matrix([
    [-4*y, 2*y],
    [2, 3]
])

matrix2 = sp.Matrix([
    [2*y, 6],
    [2, 2*x]
])

matrix3 = sp.Matrix([
    [5],
    [-5]
])

result = (matrix1 + matrix2) * matrix3
sp.pprint(result)