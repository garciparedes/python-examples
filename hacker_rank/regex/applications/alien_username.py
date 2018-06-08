#!/usr/bin/env python3

import re

import enforce

REGEX_PATTERN = r'[\._]\d+[a-zA-Z]*_?$'


@enforce.runtime_validation
def validate(s: str) -> bool:
    return re.match(REGEX_PATTERN, s) is not None


@enforce.runtime_validation
def main() -> None:
    n = int(input())
    s = ""
    for i in range(n):
        print("VALID" if validate(input()) else "INVALID")


if __name__ == '__main__':
    main()
