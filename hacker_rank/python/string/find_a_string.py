#!/usr/bin/env python3

import re

import enforce


@enforce.runtime_validation
def count_matches(string: str, sub_string: str) -> int:
    return len(re.findall(r'(?=(' + sub_string + '))', string))


@enforce.runtime_validation
def main() -> None:
    s = input().strip()
    p = input().strip()
    print(count_matches(s, p))


if __name__ == '__main__':
    main()
