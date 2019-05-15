#!/usr/bin/env python3

import math


class Complex(object):

    def __init__(self, real: float, imaginary: float = 0.0) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: 'Complex') -> 'Complex':
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __sub__(self, other: 'Complex') -> 'Complex':
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)

    def __mul__(self, other: 'Complex') -> 'Complex':
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.real * other.imaginary) + (other.real * self.imaginary)
        return Complex(real, imaginary)

    def __truediv__(self, other: 'Complex') -> 'Complex':
        denominator = (other.real ** 2 + other.imaginary ** 2)
        real = ((self.real * other.real) + (self.imaginary * other.imaginary)) / denominator
        imaginary = ((self.imaginary * other.real) - (self.real * other.imaginary)) / denominator
        return Complex(real, imaginary)

    def mod(self) -> 'Complex':
        modulus = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(modulus)

    def __str__(self) -> str:
        result = '{:0.2f}{:+0.2f}i'.format(self.real, self.imaginary)
        return result


def main():
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


if __name__ == '__main__':
    main()
