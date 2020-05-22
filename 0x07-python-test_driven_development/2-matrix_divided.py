#!/usr/bin/python3
"""
Matrix operations
"""


def matrix_divided(matrix, div):
    """ Function that divides by n the elements of a matrix"""
    matrixError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matrixError)
    if len(matrix) == 0:
        raise TypeError(matrixError)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for n in matrix:
        if not isinstance(n, list):
            raise TypeError(matrixError)
        if len(n) == 0:
            raise TypeError(matrixError)
        if len(matrix[0]) != len(n):
            raise TypeError("Each row of the matrix must have the same size")
        for m in n:
            if not isinstance(m, (int, float)):
                raise TypeError(matrixError)
    return [[round(x / div, 2) for x in y] for y in matrix]

if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")