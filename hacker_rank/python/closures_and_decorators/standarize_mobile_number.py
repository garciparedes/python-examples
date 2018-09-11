#!/usr/bin/env python3

from typing import Iterable


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def read_str_iterable() -> Iterable[int]:
    while True:
        yield read_str()


def wrapper(f):
    def fun(l, prefix='+91'):
        f(['{} {} {}'.format(prefix, phone[-10:-5], phone[-5:]) for phone in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


def main():
    phone_numbers = [read_int() for _ in range(read_int())]
    sort_phone(phone_numbers)


if __name__ == '__main__':
    main()
