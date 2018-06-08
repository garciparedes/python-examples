#!/usr/bin/env python3

import re


def custom_repl(match) -> str:
    if match.group(1) is not None:
        return match.group(1).upper()
    else:
        return match.group(2).lower()


def swap_case(s: str) -> str:
    return re.sub(r'([a-z]+)|([A-Z]+)', custom_repl, s)


def main() -> None:
    print(swap_case(input()))


if __name__ == '__main__':
    main()
