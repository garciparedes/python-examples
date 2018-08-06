#!/usr/bin/env python3


def main() -> None:
    set_a = frozenset(input().strip().split(' '))
    n = int(input().strip())
    i = 0
    is_super_set = True
    while is_super_set and i < n:
        set_i = frozenset(input().strip().split(' '))
        is_super_set = set_a.issuperset(set_i)
        i += 1
    print(is_super_set)


if __name__ == '__main__':
    main()
