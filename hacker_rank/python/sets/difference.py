#!/usr/bin/env python3


def main() -> None:
    _ = input()
    A = frozenset(input().strip().split(' '))
    _ = input()
    B = frozenset(input().strip().split(' '))
    print(len(A.difference(B)))


if __name__ == '__main__':
    main()
