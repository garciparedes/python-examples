#!/usr/bin/env python3

import re

REGEX_PATTERN = r'^(tac)(\1(tic)?)*$'

def is_matched(s: str) -> bool:
    return bool(re.search(REGEX_PATTERN, s))

def main() -> None:
    print(str(is_matched(input())).lower())


if __name__ == '__main__':
    main()
