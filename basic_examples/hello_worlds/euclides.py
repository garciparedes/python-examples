"""
Author: Sergio Garcia Prado
        www.garciparedes.me

Example of Euclides Algorithm.
"""

from pip._vendor.distlib.compat import raw_input


def euclides(m, n):
    while (m > 0):
        t = m
        m = n % m
        n = t
    return n


def main():
    print("GCD Euclides Algorithm.")

    numA = raw_input("Number A: ")
    numB = raw_input("Number B: ")

    print("GCD of %s and %s is  %s" % (numA, numB, euclides(3, 6)))


if __name__ == "__main__":
    main()
