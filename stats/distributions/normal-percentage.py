#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():

    plt.plot(np.linspace(0.5,1,100),norm.ppf(np.linspace(0.5,1,100)))
    plt.grid(True)
    plt.xlabel('alpha')
    plt.ylabel('Z_alpha')
    plt.show()

if __name__ == '__main__':
    main()
