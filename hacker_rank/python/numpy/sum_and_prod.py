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


def read_array(n: int, m: int) -> np.ndarray:
    raw_data = []
    for _ in range(n):
        raw_data.append(read_int_list())
    data = np.array(raw_data)
    return data


def main() -> None:
    n, m = read_int_list()
    data = read_array(n, m)
    result = np.prod(data.sum(axis=0))
    print(result)


if __name__ == '__main__':
    main()
