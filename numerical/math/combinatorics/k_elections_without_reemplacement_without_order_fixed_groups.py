#!/usr/bin/env python3

import scipy.special as sp_special
import numpy as np
import math

from matplotlib import pyplot as plt

from functools import reduce


combs = lambda n, k: sp_special.comb(n, k, exact=True)


def main():
    n = 4
    k = 3
    print("n =", n, "k =", k,
          "k elections without replacement =", combs(n, k))


if __name__ == '__main__':
    main()
