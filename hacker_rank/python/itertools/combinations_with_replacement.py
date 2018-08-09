#!/usr/bin/env python3

import itertools as it


def main() -> None:
    s, n = input().split(' ')
    s = sorted(s)
    n = int(n)
    print('\n'.join(
        map(lambda x: ''.join(x), it.combinations_with_replacement(s, n))
    ))


if __name__ == '__main__':
    main()
