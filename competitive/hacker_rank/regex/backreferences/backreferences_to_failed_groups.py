#!/usr/bin/env python3

import re


def main() -> None:
    regex_pattern = r'^\d{2}(-?)(\d{2}\1){2}\d{2}$'
    print(str(bool(re.search(regex_pattern, input()))).lower())


if __name__ == '__main__':
    main()
