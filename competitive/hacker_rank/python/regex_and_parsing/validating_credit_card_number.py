#!/usr/bin/env python3

import re
from typing import Set


def read_str() -> str:
    return input()


def read_int() -> int:
    return int(read_str())


def valid_characters(text: str) -> bool:
    return bool(re.match(r'^\d{16}|\d{4}(-\d{4}){3}$', text))


def valid_start_chr(text: str, start_set: Set[chr] = frozenset('456')):
    return text[0] in start_set


def consecutive_repetitions(text: str, count: int):
    return bool(re.search(r'(\d)(-?\1){3}', text))


def is_valid_credit_card_number(text: str) -> bool:
    if not valid_characters(text):
        return False

    if not valid_start_chr(text):
        return False

    if consecutive_repetitions(text, 4):
        return False

    return True


def main() -> None:
    for _ in range(read_int()):
        text = read_str()
        result = is_valid_credit_card_number(text)
        print('Valid' if result else 'Invalid')


if __name__ == '__main__':
    main()
