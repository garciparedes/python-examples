#!/usr/bin/env python3


from typing import List, Iterable, Tuple

from fractions import Fraction

import re

import itertools as it
import functools as ft


def read_str() -> str:
    return input().strip()


def yield_str() -> str:
    while True:
        yield read_str()


def read_int() -> int:
    return int(read_str())


def read_str_list() -> List[str]:
    return read_str().split()


def read_int_iterable() -> Iterable[int]:
    return map(int, read_str_list())


def yield_fraction() -> Fraction:
    while True:
        yield Fraction(*read_int_iterable())


def main() -> None:
    n = read_int()
    fractions = it.islice(yield_fraction(), n)
    result = ft.reduce(lambda a, b: a * b, fractions)
    print('{:d} {:d}'.format(result.numerator, result.denominator))


if __name__ == '__main__':
    main()
