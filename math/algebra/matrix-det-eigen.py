#!/usr/bin/env python3

import numpy as np

def main():

    a = np.matrix([[1, 0], [- 5, 7]])
    det_a = np.linalg.det(a)
    eigvals_a = np.linalg.eigvals(a)

    print("Matriz A:")
    print(a)
    print("Determinante de A:")
    print(det_a)
    print("Valores Propios de A:")
    print(eigvals_a)
    b = np.matrix([[3, 1], [2, np.sqrt(np.pi)]])
    det_b = np.linalg.det(b)
    eigvals_b = np.linalg.eigvals(b)

    print("Matriz A:")
    print(b)
    print("Determinante de B:")
    print(det_b)
    print("Valores Propios de B:")
    print(eigvals_b)

    c = np.matrix([[- 2, 0, 1], [3, 2, 4], [- 1, - 1, 0]])
    det_c = np.linalg.det(c)
    eigvals_c = np.linalg.eigvals(c)

    print("Matriz C:")
    print(c)
    print("Determinante de C:")
    print(det_c)
    print("Valores Propios de C:")
    print(eigvals_c)

if __name__ == '__main__':
    main()
