#!/usr/bin/env python3

import re


def main() -> None:
    regex_pattern = r'(.){1}(?!\1)'

    match = re.findall(Regex_Pattern, input())

    print("Number of matches :", len(match))


if __name__ == '__main__':
    main()
