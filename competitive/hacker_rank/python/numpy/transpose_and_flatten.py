#!/usr/bin/env python3

import numpy as np


def main():
    shape = list(map(int, input().split(' ')))
    a = np.zeros(shape, dtype=int)

    for i in range(shape[0]):
        a[i, :] = list(map(int, input().split(' ')))
    print(np.transpose(a))
    print(a.flatten())


if __name__ == '__main__':
    main()
