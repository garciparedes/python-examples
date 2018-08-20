#!/usr/bin/env python3

import re

import itertools as it


EMAIL_REGEX = re.compile(r'^[\w\-]+@[a-zA-Z\d]+\.[a-zA-Z]{,3}$')


def read_str() -> str:
    return input().strip()


def yield_str() -> str:
    while True:
        yield input().strip()


def read_int() -> int:
    return int(read_str())


def is_valid_email(text: str) -> bool:
    return re.search(EMAIL_REGEX, text) is not None

def main() -> None:
    n = read_int()
    possible_emails = it.islice(yield_str(), n)
    correct_emails = filter(is_valid_email, possible_emails)
    print(list(correct_emails))


if __name__ == '__main__':
    main()
