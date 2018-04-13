#!/usr/bin/env python3

import enforce

import numpy as np

@enforce.runtime_validation
def reflector(A, i: int):
    x = np.take(A, [i], 1)
    y =  np.concatenate([x[:i], [[np.sqrt(np.sum(np.power(x[i:],2)))]],
                        np.zeros([A.shape[0] - i - 1, 1])])
    u = (x - y)
    return np.eye(A.shape[0]) - (2 / np.squeeze(u.T @ u)) * (u @ u.T)

@enforce.runtime_validation
def qr_householder(A):
    Q = np.eye(A.shape[0])
    for i in range(A.shape[1]):
        R = reflector(A, i)
        Q = Q @ R
        A = R @ A
    return (Q, A)

def main() -> None:

    A = np.array([[1,-1,1],
                [1,1,1],
                [1,1,-1],
                [1,1,1]])

    b = np.array([1, 1, -1, 0])

    [Q, R] = qr_householder(A)
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
