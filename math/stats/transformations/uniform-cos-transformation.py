#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():

    bins = 100

    elems_per_bin = 10 ** 5

    x = np.random.uniform(0,2*np.pi, bins * elems_per_bin)
    y = np.cos(x)

    f_x = np.histogram(x, bins)[0] / (elems_per_bin*(np.max(x)-np.min(x)))
    f_y = np.histogram(y, bins)[0]/ (elems_per_bin*(np.max(y)-np.min(y)))

    plt.plot(np.linspace(np.min(x),np.max(x),bins),f_x)
    plt.plot(np.linspace(np.min(y),np.max(y),bins),f_y)

    plt.gca().set_ylim([0,1])
    plt.yticks(np.arange(0,1,0.1))
    plt.grid(True)

    plt.show()

if __name__ == '__main__':
    main()
