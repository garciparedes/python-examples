#!/usr/bin/env python3

import textwrap


def wrap(s: str, w: int) -> str:
    return '\n'.join(textwrap.wrap(s, w))


def main() -> None:
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


if __name__ == '__main__':
    main()
