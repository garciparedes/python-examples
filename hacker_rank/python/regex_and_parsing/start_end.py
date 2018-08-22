#!/usr/bin/env python3

from typing import List

import re


def read_str() -> str:
    return input().strip()


def find_by_pattern(text: str, pattern: str) -> List:
    return list(re.finditer(r'(?=({}))'.format(pattern), text))


def main() -> None:
    text = read_str()
    pattern = read_str()
    matches = find_by_pattern(text, pattern)

    if matches:
        for match in matches:
            print((match.start(1), match.end(1) - 1))
    else:
        print((-1, -1))


if __name__ == '__main__':
    main()
