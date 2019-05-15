#!/usr/bin/env python3

import re

REPEATED_REGEX = re.compile(r'([a-zA-Z0-9])\1')


def read_str() -> str:
    return input().strip()


def find_first_duplicate(text: str) -> str:
    occurrence = re.search(REPEATED_REGEX, text)

    if not occurrence:
        return '-1'

    return occurrence.group(1)


def main() -> None:
    text = read_str()
    print(find_first_duplicate(text))


if __name__ == '__main__':
    main()
