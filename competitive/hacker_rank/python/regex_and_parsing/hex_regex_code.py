#!/usr/bin/env python3

from typing import Iterable

import re


HEX_COLOR_REGEX = re.compile(r'(?<!^)#([\da-fA-F]{3}){1,2}(?!\s|$)')


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def find_hex_colors(text: str) -> Iterable:
    return re.finditer(HEX_COLOR_REGEX, text)


def main() -> None:
    text = str()
    for _ in range(read_int()):
        text += read_str()
        text += '\n'

    hex_colors = find_hex_colors(text)

    for hex in hex_colors:
        print(hex.group(0))


if __name__ == '__main__':
    main()
