"""
Author: Sergio Garcia Prado
        www.garciparedes.me
""""

from random import randint

dimension = 30

matrix = [[0 for x in range(dimension)] for x in range(dimension)]

for i in range(len(matrix)):
    linea = ""
    for j in range (len(matrix[i])):
        matrix [i][j] = randint(0,1)
        linea += str(matrix[i][j])
    print linea
