#!/usr/bin/env python3

from collections import Counter
from functools import reduce


def f(cnt: Counter, shape: str, price) -> int:
    if cnt[shape] > 0:
        cnt[shape] -= 1
        return int(price)
    else:
        return 0


def main() -> None:
    _ = int(input())
    x = input().split()
    cnt = Counter(x)
    c_n = int(input())
    print(reduce(lambda a, b: a + b,
                 map(lambda _: f(cnt, *input().split()),
                     range(c_n))
                 )
          )


if __name__ == '__main__':
    main()
