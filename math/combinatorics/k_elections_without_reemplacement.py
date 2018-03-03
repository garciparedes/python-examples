#!/usr/bin/env python3

import scipy as sp
import numpy as np
import math

from matplotlib import pyplot as plt

from functools import reduce


combs = lambda n, k: reduce(lambda a, b: a * b, range(n-k+1, n+1))


def main():
    n = 4
    k = 3
    print("n =", n, "k =", k,
          "k elections without replacement =", combs(n, k))


if __name__ == '__main__':
    main()
