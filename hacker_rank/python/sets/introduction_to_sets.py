#!/usr/bin/env python3

from typing import List, Union
from functools import reduce
import enforce

Num = Union[int, float]


@enforce.runtime_validation
def average(array: List[Num]) -> float:
    x = set(array)
    return reduce(lambda a, b: a + b, x) / float(len(x))


@enforce.runtime_validation
def main() -> None:
    _ = int(input())
    arr = list(map(int, input().split()))
    print(average(arr))


if __name__ == '__main__':
    main()
