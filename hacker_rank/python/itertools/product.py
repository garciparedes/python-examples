#!/usr/bin/env python3

import itertools as it

import enforce


@enforce.runtime_validation
def main() -> None:
    a = input().split(' ')
    b = input().split(' ')
    print(' '.join(map(lambda x: '({}, {})'.format(*x), it.product(a, b))))


if __name__ == '__main__':
    main()
