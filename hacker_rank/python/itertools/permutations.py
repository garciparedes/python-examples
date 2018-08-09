#!/usr/bin/env python3

import itertools as it


def main() -> None:
    s, n = input().split(' ')
    print('\n'.join(map(lambda x: ''.join(x), it.permutations(sorted(s), int(n)))))


if __name__ == '__main__':
    main()
