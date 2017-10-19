#! /usr/bin/python3

import numpy as np
from scipy import stats, integrate

def integrate_function(f, a1, a2, b1, b2):
    return integrate.dblquad(f, a1, a2, b1 , b2)[0]


def main():

    e_19_3 = integrate_function(lambda y, x: x * y ** 2, -1, 1, lambda x: -x, lambda x: x)
    print("E19.1:\t" + str(e_19_3))

    e_19_3 = integrate_function(lambda y, x: x ** 2 + y ** 2, 0, 1, lambda x: x ** 3, lambda x: x ** 2)
    print("E19.2:\t" + str(e_19_3))

    e_19_3 = integrate_function(lambda y, x: (x * y - y ** 2) ** (1 / 2), 0, 1, lambda x: 0, lambda x: x)
    print("E19.3:\t" + str(e_19_3))

if __name__ == '__main__':
    main()
