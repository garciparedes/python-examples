#!/usr/bin/env python3

import numpy as np

def truncate_digits(value, digits=None):
    if digits is None:
        return value
    else:
        sign = value < 0
        value = abs(value) % 10 ** digits
        shift = 0
        while digits > shift and value > 1:
            shift += 1
            value = value / 10
        value = np.round(value, decimals=digits) * 10 ** shift
        if sign == True:
            value *= - 1
        return value


def direct_eval(polinomial, x_0, digits=None):
    r = 0.0

    cached = np.ones(polinomial.shape[0])

    for i in range(1, polinomial.shape[0]):
        cached[i] = truncate_digits(cached[i - 1] * x_0, digits=digits)

    for i in range(polinomial.shape[0]):
        r = truncate_digits(r + truncate_digits(cached[i] * polinomial[i],
                            digits=digits), digits=digits)
    return r



def nested_eval(polinomial, x_0, digits=None):
    r = 0.0
    for i in reversed(range(1, polinomial.shape[0])):
        r = truncate_digits(x_0 * truncate_digits(r + polinomial[i],
                digits=digits), digits=digits)
    return truncate_digits(r + truncate_digits(polinomial[0], digits=digits),
                           digits=digits)



def main():

    p_x = np.array([- 0.149, 3, - 6, 1])
    x_0 = 4.71
    print(direct_eval(p_x, x_0, 3))
    print(nested_eval(p_x, x_0, 3))
    pass

if __name__ == '__main__':
    main()
