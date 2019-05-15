#!/usr/bin/env python3

import re


def count_matches(string: str, sub_string: str) -> int:
    return len(re.findall(r'(?=(' + sub_string + '))', string))


def main() -> None:
    s = input().strip()
    p = input().strip()
    print(count_matches(s, p))


if __name__ == '__main__':
    main()
