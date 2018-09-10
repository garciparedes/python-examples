#!/usr/bin/env python3

import re


def read_str() -> str:
    return input()


def read_int() -> int:
    return int(read_str())


def valid_characters(text: str) -> bool:
    return bool(re.match(r'^[1-9]\d{5}$', text))


def contains_alternating_pair(text: str, k: int = 2) -> bool:
    return len(re.findall(r'(\d)(?=\d\1)', text)) < k


def is_valid_postal_code(text: str) -> bool:
    if not valid_characters(text):
        return False

    if contains_alternating_pair(text):
        return False

    return True


def main() -> None:
    text = read_str()
    result = is_valid_postal_code(text)
    print(result)


if __name__ == '__main__':
    main()
