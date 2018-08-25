#!/usr/bin/env python3

import re

PHONE_NUMBER_REGEX = re.compile(r'^[789]\d{9}$')


def read_str() -> str:
    return input()


def read_int() -> int:
    return int(read_str())


def is_valid_phone_number(text: str) -> bool:
    return bool(re.match(PHONE_NUMBER_REGEX, text))


def main() -> None:
    for _ in range(read_int()):
        text = read_str()
        result = is_valid_phone_number(text)
        print('YES' if result else 'NO')


if __name__ == '__main__':
    main()
