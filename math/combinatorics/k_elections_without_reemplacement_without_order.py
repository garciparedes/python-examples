#!/usr/bin/env python3

import scipy.special as sp_special
import numpy as np
import math

from matplotlib import pyplot as plt

from functools import reduce


combs = lambda n, n_i: sp_special.factorial(n) / np.prod(sp_special.factorial(n_i))


def main():
    n = 5
    n_i = np.array([2, 2, 1])
    print("n =", n, "n_i =", n_i,
          "k elections without replacement =", combs(n, n_i))


if __name__ == '__main__':
    main()
