#!/usr/bin/env python3

import re

ROMAN_NUMBER_REGEX = re.compile(r'^(((?P<s1>[IXCM]){1,3}|(?P<s2>[VLD]){1}|(?P<s3>[VLD]){3})(?!(?P=s1)|(?P=s2)|(?P=s3)))+$')


def read_str() -> str:
    return input()


def is_valid_roman_number(text: str) -> bool:
    return bool(re.match(ROMAN_NUMBER_REGEX, text))


def main() -> None:
    text = read_str()
    result = is_valid_roman_number(text)
    print(result)


if __name__ == '__main__':
    main()
