#!/usr/bin/env python3

from collections import defaultdict


def main() -> None:
    n, m = map(int, input().strip().split())
    d = defaultdict(list)

    for i in range(1, n + 1):
        d[input().strip()].append(i)

    for i in range(m):
        print(' '.join(map(str, d[input().strip()] or [-1])))


if __name__ == '__main__':
    main()
