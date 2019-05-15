#!/usr/bin/env python3

import numpy as np


def main():
    A = np.array(list(map(float, input().strip().split(' '))))

    print(np.floor(A), np.ceil(A), np.rint(A), sep="\n")


if __name__ == '__main__':
    main()
