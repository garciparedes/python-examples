#!/usr/bin/env python3

import itertools as it
from math import pow


def integers_come_in_all_sizes(a: int, b: int, c: int, d: int) -> int:
    return a ** b + c ** d

def int_line_reader() -> int:
    while True:
        yield int(input().strip())


def main() -> None:
    a, b, c, d = it.islice(int_line_reader(), 4)
    print(integers_come_in_all_sizes(a, b, c, d))


if __name__ == '__main__':
    main()
