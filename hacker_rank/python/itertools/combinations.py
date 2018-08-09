#!/usr/bin/env python3

import itertools as it


def main() -> None:
    s, n = input().split(' ')
    s = sorted(s)
    n = int(n)
    print('\n'.join(
        map(lambda x: ''.join(x),
            it.chain(
                *map(lambda i: it.combinations(s, i),
                     range(1, n + 1))
            )
        )
    ))


if __name__ == '__main__':
    main()
