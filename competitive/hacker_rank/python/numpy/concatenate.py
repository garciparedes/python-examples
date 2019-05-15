#!/usr/bin/env python3

import numpy as np


def main():
    shape = list(map(int, input().split(' ')))

    a = np.zeros([shape[0], shape[2]], dtype=int)
    b = np.zeros([shape[1], shape[2]], dtype=int)

    for i in range(shape[0]):
        a[i][:] = list(map(int, input().split(' ')))
    for i in range(shape[1]):
        b[i][:] = list(map(int, input().split(' ')))

    print(np.concatenate((a, b), axis=0))


if __name__ == '__main__':
    main()
