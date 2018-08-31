#!/usr/bin/env python3

from typing import List, Iterable

import numpy as np


def read_str() -> str:
    return input().strip()


def read_str_list() -> List[str]:
    return read_str().split(' ')


def read_int_iterable() -> Iterable[int]:
    return map(int, read_str_list())


def read_int_list() -> List[int]:
    return list(read_int_iterable())


def main() -> None:
    a = read_int_list()
    b = read_int_list()

    print(np.inner(a, b))
    print(np.outer(a, b))


if __name__ == '__main__':
    main()
