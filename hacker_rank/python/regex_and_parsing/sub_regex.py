#!/usr/bin/env python3

import re

TO_REPLACE_REGEX = re.compile(r'(?<= )((&&)|(\|\|))(?= )')

REPLACE_DICT = {
    '&&': 'and',
    '||': 'or',
}


def read_str() -> str:
    return input()


def read_int() -> int:
    return int(read_str().strip())


def replace_with_dict(text: str) -> str:
    return re.sub(TO_REPLACE_REGEX, lambda x: REPLACE_DICT[x.group()], text)


def main() -> None:
    for _ in range(read_int()):
        text = read_str()
        result = replace_with_dict(text)
        print(result)


if __name__ == '__main__':
    main()
