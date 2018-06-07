#!/bin/python3

from typing import List

import enforce


@enforce.runtime_validation
def generate_list(x: int, y: int, z: int, n: int) -> List[List[int]]:
    arr = list()
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k is not n:
                    arr.append([i, j, k])
    return arr


@enforce.runtime_validation
def main() -> None:
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(generate_list(x, y, z, n))


if __name__ == '__main__':
    main()
