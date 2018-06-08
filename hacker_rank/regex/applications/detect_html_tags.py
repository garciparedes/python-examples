#!/usr/bin/env python3

import re

REGEX_PATTERN = r'<([^/]+?)(?: .*?)?>'


def find_matches(s: str):
    return set(re.findall(REGEX_PATTERN, s, re.MULTILINE))


def main() -> None:
    n = int(input())
    s = ""
    for i in range(n):
        s += input()
    print(';'.join(sorted(find_matches(s))))


if __name__ == '__main__':
    main()
