#!/usr/bin/env python3

from typing import List

import re

VOWELS = 'aeiouAEIOU'

REPEATED_VOWELS_REGEX = re.compile('(?<=[^{0}])[{0}]{{2,}}(?=[^{0}])'.format(VOWELS))


def read_str() -> str:
    return input().strip()


def repeated_vowels_iterable(text: str) -> List:
    return re.findall(REPEATED_VOWELS_REGEX, text)


def main() -> None:
    text = read_str()
    matches = repeated_vowels_iterable(text)

    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)


if __name__ == '__main__':
    main()
