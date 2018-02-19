#!/usr/bin/env python3

import numpy as np
import re

def truncate_digits(value, decimals):
    return np.round(value, decimals=decimals)


def direct_eval(polinomial, x_0, digits):
    r = 0.0

    cached = np.ones(polinomial.shape[0])

    for i in range(1, polinomial.shape[0]):
        cached[i] = cached[i - 1] * x_0

    for i in range(polinomial.shape[0]):
        r += truncate_digits(cached[i] * polinomial[i], decimals=digits)

    return r



def nested_eval(polinomial, x_0, digits):
    r = 0.0
    for i in reversed(range(1, polinomial.shape[0])):
        r = truncate_digits(x_0 * truncate_digits(r + polinomial[i],
                decimals=digits), decimals=digits)
    r += truncate_digits(polinomial[0], decimals=digits)
    return r



def main():

    p_x = np.array([- 0.149, 3, - 6, 1])
    x_0 = 4.71
    print(direct_eval(p_x, x_0, 3))
    print(nested_eval(p_x, x_0, 3))
    pass

if __name__ == '__main__':
    main()
