import sympy as sp

x, y = sp.symbols("x y")


matrix1 = sp.Matrix([
    [6*y, y**2],
    [-2*y, -2*y]])

matrix2 = sp.Matrix([
    [-y, x*y],
    [-6, x**2]])

matrix3 = sp.Matrix([
    [6*y, -6],
    [-3*y, y]])


result = matrix1 * matrix2 - matrix3

sp.pprint(result)