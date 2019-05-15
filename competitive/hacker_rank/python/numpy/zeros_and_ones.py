#!/usr/bin/env python3

import numpy as np


def main():
    shape = list(map(int, input().split(' ')))

    print(np.zeros(shape, dtype=int))
    print(np.ones(shape, dtype=int))


if __name__ == '__main__':
    main()
