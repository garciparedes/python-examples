#!/usr/bin/env python3

import re
from collections import Counter


def read_str() -> str:
    return input()


def read_int() -> int:
    return int(read_str())


def valid_characters(text: str) -> bool:
    return bool(re.match(r'^[a-zA-Z0-9]{10}$', text))


def upper_case_count(text: str) -> int:
    return len(re.findall(r'[A-Z]', text))


def digits_count(text: str) -> int:
    return len(re.findall(r'\d', text))


def repeated_characters(text: str) -> bool:
    return Counter(text).most_common(1)[0][1] > 1


def is_valid_uid(text: str) -> bool:
    if not valid_characters(text):
        return False

    if not upper_case_count(text) >= 2:
        return False

    if not digits_count(text) >= 3:
        return False

    if repeated_characters(text):
        return False

    return True


def main() -> None:
    for _ in range(read_int()):
        text = read_str()
        result = is_valid_uid(text)
        print('Valid' if result else 'Invalid')


if __name__ == '__main__':
    main()
