#!/usr/bin/env python3

import numpy as np


def arrays(arr: list) -> np.ndarray:
    return np.flip(np.array(arr, dtype=np.float64), 0)


def main():
    l = input().split(' ')
    l_np = arrays(l)
    print(l_np)


if __name__ == '__main__':
    main()
