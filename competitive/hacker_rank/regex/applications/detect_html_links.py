#!/usr/bin/env python3

import re

REGEX_PATTERN = r'<a .*?href="(\S+)"[^<]*?>(.*?)</a>'
REGEX_CLEAN = r"(?:<.*?/>)|(?:<(.+?)>(.+?)</\1>)"
REGEX_SUB = r"\2"


def remove_recursive(s: str) -> str:
    s_cleaned = re.sub(REGEX_CLEAN, REGEX_SUB, s)
    while s_cleaned != s:
        s = s_cleaned
        s_cleaned = re.sub(REGEX_CLEAN, REGEX_SUB, s)
    return s_cleaned.strip()


def find_matches(s: str):
    matches = re.findall(REGEX_PATTERN, s, re.MULTILINE)
    matches = [list(m) for m in matches]
    for i in range(len(matches)):
        matches[i][1] = remove_recursive(matches[i][1])

    return matches


def main() -> None:
    n = int(input())
    s = ""
    for i in range(n):
        s += input()

    for m in find_matches(s):
        print(','.join(m))


if __name__ == '__main__':
    main()
