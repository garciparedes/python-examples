#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    '''
        X -> LogNormal(nu, sigma)
        P(X<40) = 0.4
        P(X<50) = 0.55
    '''

    perc1 = 0.4
    p1 = 40

    perc2 = 0.55
    p2 = 50

    z_04  = norm.ppf(perc1)
    z_055 = norm.ppf(perc2)

    sigma = (np.log(p1)-np.log(p2))/(z_04 - z_055)
    nu = (z_055 * sigma + np.log(40))

    print('nu = ' + str(nu))
    print('sigma = ' + str(sigma))

if __name__ == '__main__':
    main()
