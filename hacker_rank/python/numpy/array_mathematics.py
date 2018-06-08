#!/usr/bin/env python3

import numpy as np


def main():
    [n, m] = map(int, input().strip().split(" "))

    A = []
    for i in range(n):
        A.append(list(map(int, input().strip().split(" "))))

    B = []
    for i in range(n):
        B.append(list(map(int, input().strip().split(" "))))

    A_np = np.array(A, dtype=int)
    B_np = np.array(B, dtype=int)

    print(A_np + B_np)


if __name__ == '__main__':
    main()
