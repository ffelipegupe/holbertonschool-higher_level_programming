#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x * x for x in matrix[i]] for i in range(len(matrix))]
    
