#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
     for row in matrix:
         new_row = []
        for num in row:
            new_row.append(num ** 2)
        result_matrix.append(new_row)
     return result_matrix
