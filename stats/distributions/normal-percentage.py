#! /usr/bin/python3

import numpy as np
from sympy import *
from mpmath import gamma, e

def main():

    a = 0
    b = oo

    x = Symbol('x')
    k = 2 #Symbol('k')

    f = (x ** (k / 2 - 1) * e ** (-x / 2)) / (2 ** (k / 2) * gamma(k / 2))
    g = 1 / x

    print(sympify(integrate( g * f, (x, a,b))))

if __name__ == '__main__':
    main()
