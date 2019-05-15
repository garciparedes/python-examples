#!/usr/bin/env python3

import numpy as np


def main():
    shape = list(map(int, input().split(' ')))
    print(np.eye(shape[0], shape[1]))


if __name__ == '__main__':
    main()
