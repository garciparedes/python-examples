#!/usr/bin/env python3

import re

REGEX_PATTERN = r'(?<=[13579])\d'

def find_matches(s: str):
    re.findall(REGEX_PATTERN, s)

def main() -> None:
    print("Number of matches :", len(find_matches(input())))


if __name__ == '__main__':
    main()
