#!/usr/bin/env python3

from typing import List, Iterable

import numpy as np


def read_str() -> str:
    return input().strip()


def read_str_list() -> List[str]:
    return read_str().split(' ')


def read_float() -> float:
    return float(read_str())


def read_float_iterable() -> Iterable[float]:
    return map(float, read_str_list())


def read_float_list() -> List[float]:
    return list(read_float_iterable())


def main() -> None:
    c = np.array(read_float_list())
    x = read_float()

    y = np.polyval(c, x)
    print(y)


if __name__ == '__main__':
    main()
