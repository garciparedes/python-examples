#!/usr/bin/env python3

from typing import Iterable, Dict, Any

import re

REPLACE_DICT = {
    '&&': 'and',
    '||': 'or',
}


def keys_to_regex_groups(dictionary: Dict[str, Any]) -> Iterable[str]:
    return map(lambda x: f'({re.escape(x)})', dictionary.keys())


def alternatives_to_regex(alternatives: Iterable[str]) -> str:
    return '|'.join(alternatives)


TO_REPLACE_REGEX = re.compile(r'(?<= )({})(?= )'.format(alternatives_to_regex(keys_to_regex_groups(REPLACE_DICT))))


def read_str() -> str:
    return input()


def read_int() -> int:
    return int(read_str().strip())


def replace_with_dict(text: str) -> str:
    return re.sub(TO_REPLACE_REGEX, lambda x: REPLACE_DICT[x.group()], text)


def main() -> None:
    print(TO_REPLACE_REGEX)
    for _ in range(read_int()):
        text = read_str()
        result = replace_with_dict(text)
        print(result)


if __name__ == '__main__':
    main()
