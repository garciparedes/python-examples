#!/usr/bin/env python3

import math

import enforce

ROW_FORMAT = "{:>{offset}d} {:>{offset}o} {:>{offset}X} {:>{offset}b}"


@enforce.runtime_validation
def print_formatted(n: int) -> None:
    offset = 1 + math.floor(math.log2(n))
    print('\n'.join(map(lambda i: ROW_FORMAT.format(*([i] * 4), offset=offset),
                        range(1, n + 1))))


@enforce.runtime_validation
def main() -> None:
    print_formatted(int(input()))


if __name__ == '__main__':
    main()
