#!/usr/bin/env python3

import numpy as np
from scipy import stats, integrate
import cmath


def integrate_function(f, a1, a2, b1, b2):
    return integrate.dblquad(f, a1, a2, b1 , b2)[0]


def main():

    e_19_1 = integrate_function(lambda y, x: x * y ** 2, -1, 1,
                                lambda x: -x, lambda x: x)

    print("E19.1:\t" + str(e_19_1))

    e_19_2 = integrate_function(lambda y, x: x ** 2 + y ** 2, 0, 1,
                                lambda x: x ** 3, lambda x: x ** 2)
    print("E19.2:\t" + str(e_19_2))

    e_19_3 = integrate_function(lambda y, x: (x * y - y ** 2) ** (1 / 2), 0, 1,
                                lambda x: 0, lambda x: x)
    print("E19.3:\t" + str(e_19_3))

    e_19_4 = integrate_function(lambda x, y: 12 - 3 * x - 4 * y , 0, 1,
                                lambda b: b ** 2, lambda b: 3 - 2 * b)
    print("E19.4:\t" + str(e_19_4))

    e_19_5 = integrate_function(lambda y, x: x ** 2 + y ** 2, - np.sqrt(2), 1,
                                lambda b1: b1 ** 2, lambda b2: 2)
    print("E19.5:\t" + str(e_19_5))

    e_19_6 = integrate_function(lambda y, x: y ** 2, -2, 6,
                                lambda b1: np.abs(b1), lambda b2: np.divide(b2,2) + 3)
    print("E19.6:\t" + str(e_19_6))


    e_19_7 = integrate_function(lambda y, x: 2 * cmath.sqrt(1 - x ** 2 ).real + 1,
                                - np.arccos(0.5), np.arccos(0.5),
                                lambda b1: 1 - cmath.sqrt(1 - b1 ** 2).real,
                                lambda b2: cmath.sqrt(1 - b2 ** 2 ).real)
    print("E19.7:\t" + str(e_19_7))



    e24_1 = integrate_function(lambda y, x: 1, 0, 1,
                               lambda b1: 0, lambda b2: b2 ** 2)
    print("E24.1:\t" + str(e24_1))

    e24_3 = integrate_function(lambda y, x: y * np.sin(x), 0, np.pi / 2,
                               lambda b1: 0, lambda b2: np.cos(b2))
    print("E24.3:\t" + str(e24_3))


    e27_1 = integrate_function(lambda y, x: x * y, 0, 1,
                               lambda b1: b1, lambda b2: 1)
    print("E27.1:\t" + str(e27_1))



if __name__ == '__main__':
    main()
