#!/usr/bin/env python3

import re

FLOATING_POINT_REGEX = re.compile(r'^[+\-]?\d*\.\d+$')


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def is_floating_point_number(text: str) -> bool:
    return re.search(FLOATING_POINT_REGEX, text) is not None


def main() -> None:
    for _ in range(read_int()):
        text = read_str()
        print(is_floating_point_number(text))


if __name__ == '__main__':
    main()
