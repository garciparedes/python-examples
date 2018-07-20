#!/usr/bin/env python3

from typing import Iterable
import itertools as it


def read_int() -> Iterable[int]:
    while True:
        yield int(input().strip())


def main() -> None:
    a, b = it.islice(read_int(), 2)

    print(a // b, a % b, divmod(a, b), sep="\n")


if __name__ == '__main__':
    main()
