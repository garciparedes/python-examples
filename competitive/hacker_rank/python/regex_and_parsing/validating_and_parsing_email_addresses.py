#!/usr/bin/env python3

from collections import namedtuple
import re
import email.utils


EMAIL_REGEX = re.compile(r'^[a-zA-Z][\w\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

NameEmail = namedtuple('NameEmail', ['name', 'email'])


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def is_valid_email(text: str) -> bool:
    return bool(re.match(EMAIL_REGEX, text))


def read_name_email_tuple() -> NameEmail:
    name_email = NameEmail._make(email.utils.parseaddr(read_str()))

    if not is_valid_email(name_email.email):
        name_email = NameEmail('', '')
    return name_email


def main() -> None:
    for _ in range(read_int()):
        name_email = read_name_email_tuple()
        if name_email.name and name_email.email:
            print(email.utils.formataddr(name_email))


if __name__ == '__main__':
    main()
