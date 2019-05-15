#!/usr/bin/env python3

from typing import Iterable, Tuple
import itertools as it


def compress_the_string(s: str) -> Iterable[Tuple[int, int]]:
    grouped = it.groupby(s)
    grouped = map(lambda x: (len(list(x[1])), int(x[0])), grouped)
    return grouped


def main() -> None:
    s = input().strip()
    print(' '.join(map(str, compress_the_string(s))))


if __name__ == '__main__':
    main()
