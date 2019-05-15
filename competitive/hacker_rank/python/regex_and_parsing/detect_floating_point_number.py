#!/usr/bin/env python3

import re
import itertools as it


FLOATING_POINT_REGEX = re.compile(r'^[+\-]?\d*\.\d+$')


def read_str() -> str:
    return input().strip()


def yield_str() -> str:
    while True:
        yield input().strip()


def read_int() -> int:
    return int(read_str())


def is_floating_point_number(text: str) -> bool:
    return re.search(FLOATING_POINT_REGEX, text) is not None


def main() -> None:
    possible_floats = it.islice(yield_str(), read_int())
    are_floats = map(lambda text: str(is_floating_point_number(text)), possible_floats)
    print('\n'.join(are_floats))


if __name__ == '__main__':
    main()
