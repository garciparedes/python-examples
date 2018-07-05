#!/usr/bin/env python3


def read_set_line():
    return frozenset(map(int, input().strip().split()))


def main() -> None:
    m = int(input().strip())
    set_a = read_set_line()
    n = int(input().strip())
    set_b = read_set_line()

    assert (m == len(set_a) and n == len(set_b))

    print('\n'.join(map(str, sorted(set_a.symmetric_difference(set_b)))))


if __name__ == '__main__':
    main()
