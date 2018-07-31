#!/usr/bin/env python3

def read_frozen_set_line():
    return frozenset(input().strip().split(' '))


def main() -> None:
    for _ in range(int(input().strip())):
        _ = input()
        A = read_frozen_set_line()
        _ = input()
        B = read_frozen_set_line()
        print(A.issubset(B))


if __name__ == '__main__':
    main()
