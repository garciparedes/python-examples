#!/usr/bin/env python3

from itertools import chain
from string import ascii_lowercase


def print_rangoli(size: int) -> None:
    s = list()
    for i in reversed(range(size)):
        s.append('-'.join(
            chain(reversed(ascii_lowercase[(i + 1):size]),
                  ascii_lowercase[i:size])
        ).center((size - 1) * 4 + 1, "-"))
    print('\n'.join(chain(s, reversed(s[:-1]))))


def main() -> None:
    print_rangoli(int(input()))


if __name__ == '__main__':
    main()
