#!/bin/python

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length_i = len(i)
        if length_i == 0:
            print("")
        for x in range(length_i):
            print('{:d}'.format(i[x]))
