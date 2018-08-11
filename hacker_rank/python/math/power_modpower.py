#!/usr/bin/env python3

from typing import Iterable
import itertools as it


def read_int() -> Iterable[int]:
    while True:
        yield int(input().strip())


def main() -> None:
    a, b, m = it.islice(read_int(), 3)

    print(pow(a, b), pow(a, b, m), sep="\n")


if __name__ == '__main__':
    main()
