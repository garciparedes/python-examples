#!/usr/bin/env python3

from typing import List, Iterable

import numpy as np


def read_str() -> str:
    return input().strip()


def read_str_list() -> List[str]:
    return read_str().split(' ')


def read_int() -> int:
    return int(read_str())


def read_int_iterable() -> Iterable[int]:
    return map(int, read_str_list())


def read_int_list() -> List[int]:
    return list(read_int_iterable())


def read_array(n: int, m: int) -> np.ndarray:
    raw_data = []
    for _ in range(n):
        raw_data.append(read_int_list())
    data = np.array(raw_data)
    return data


def main() -> None:
    n = read_int()
    a = read_array(n, n)
    b = read_array(n, n)
    print(a @ b)


if __name__ == '__main__':
    main()
