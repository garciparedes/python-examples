#! /usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

def main():

    plt.plot(np.linspace(0.5,1,200),stats.norm.ppf(np.linspace(0.5,1,200)))
    plt.grid(True)
    plt.xlabel('alpha')
    plt.ylabel('Z_alpha')
    plt.show()

if __name__ == '__main__':
    main()
