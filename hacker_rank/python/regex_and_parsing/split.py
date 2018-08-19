#!/usr/bin/env python3

from typing import List

import re

COMMA_DOT_REGEX = re.compile(r'[,\.]')


def read_str() -> str:
    return input().strip()


def split_with_regex(text: str, REGEX: re.Pattern = COMMA_DOT_REGEX) -> List[str]:
    return re.split(REGEX, text)


def main() -> None:
    text = read_str()
    print('\n'.join(split_with_regex(text)))


if __name__ == '__main__':
    main()
