#!/usr/bin/env python3

import functools as ft


def read_str() -> str:
    return input().strip()


def compare_same_level(a, b) -> int:
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1


def is_chr_odd(c: chr) -> int:
    return c.isdigit() and int(c) % 2 == 1


def ginorts_comparator(a: str, b: str) -> int:
    if a.islower() and not b.islower():
        return -1
    elif not a.islower() and b.islower():
        return 1

    if a.isupper() and not b.isupper():
        return -1
    elif not a.isupper() and b.isupper():
        return 1

    if is_chr_odd(a) and not is_chr_odd(b):
        return -1
    elif not is_chr_odd(a) and is_chr_odd(b):
        return 1

    return compare_same_level(a, b)


def main() -> None:
    text = read_str()
    text = sorted(text, key=ft.cmp_to_key(ginorts_comparator))
    print(''.join(text))


if __name__ == '__main__':
    main()
