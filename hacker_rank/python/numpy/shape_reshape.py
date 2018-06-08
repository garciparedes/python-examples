#!/usr/bin/env python3

import numpy as np


def main():
    l = input().split(' ')
    l_np = np.array(l, dtype=int)
    print(np.reshape(l_np, (3, 3)))


if __name__ == '__main__':
    main()
