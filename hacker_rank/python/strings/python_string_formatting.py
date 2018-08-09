#!/usr/bin/env python3

import math


ROW_FORMAT = "{:>{offset}d} {:>{offset}o} {:>{offset}X} {:>{offset}b}"


def print_formatted(n: int) -> None:
    offset = 1 + math.floor(math.log2(n))
    print('\n'.join(map(lambda i: ROW_FORMAT.format(*([i] * 4), offset=offset),
                        range(1, n + 1))))


def main() -> None:
    print_formatted(int(input()))


if __name__ == '__main__':
    main()
