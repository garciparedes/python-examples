#!/usr/bin/env python3

from collections import Counter


def read_int_line() -> int:
    return int(input().strip())


def read_counter_line():
    return Counter(input().strip().split(' '))


def main() -> None:
    k = read_int_line()
    cnt = read_counter_line()

    print(cnt.most_common()[-1][0])


if __name__ == '__main__':
    main()
