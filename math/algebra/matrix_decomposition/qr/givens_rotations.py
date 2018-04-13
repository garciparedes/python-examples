#!/usr/bin/env python3

import enforce

import numpy as np

@enforce.runtime_validation
def rotator(A, i: int, j: int, k: int):
    G = np.eye(A.shape[0])
    r = np.sqrt(A[i, k] ** 2 + A[j, k] ** 2)
    if A[j, k] != 0:
        G[i, i] = A[i, k] / r
        G[i, j] = A[j, k] / r
        G[j, i] = - A[j, k] / r
        G[j, j] = A[i, k] / r
    return G

@enforce.runtime_validation
def qr_givens(A):
    Q = np.eye(A.shape[0])
    for j in range(A.shape[1]):
        G = np.eye(A.shape[0])
        for i in reversed(range(j, A.shape[1])):
            G = rotator(G @ A, i, i + 1, j) @ G
        Q = Q @ np.transpose(G)
        A = G @ A
    return (Q, A)

def main() -> None:

    A = np.array([[1,-1,1],
                [1,1,1],
                [1,1,-1],
                [1,1,1]])

    b = np.array([1, 1, -1, 0])

    [Q, R] = qr_givens(A)
    c = (np.transpose(Q) @ b).flatten()
    x = np.linalg.solve(R[0:R.shape[1], :], c[0:R.shape[1]])

    print("A =", np.round(A, decimals=2),  '\n', sep='\n')
    print("Q =", np.round(Q, decimals=2),  '\n', sep='\n')
    print("R =", np.round(R, decimals=2),  '\n', sep='\n')
    print("Q @ R =", np.round(Q @ R, decimals=2), '\n', sep='\n')
    print("b =", np.round(b, decimals=2), '\n', sep='\n')
    print("c =", np.round(c, decimals=2), '\n', sep='\n')
    print("x =", np.round(x, decimals=2), '\n', sep='\n')

if __name__ == '__main__':
    main()
