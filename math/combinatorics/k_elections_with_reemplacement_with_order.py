#!/usr/bin/env python3

import scipy as sp
import numpy as np
import math
from matplotlib import pyplot as plt


combs = lambda n, k: n ** k


def main():
    n = 4
    k = 3
    print("n =", n, "k =", k,
          "k elections with replacement =", combs(n, k))


if __name__ == '__main__':
    main()
