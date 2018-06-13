#!/usr/bin/env python3


import textwrap

import enforce


@enforce.runtime_validation
def wrap(s: str, w: int) -> str:
    return '\n'.join(textwrap.wrap(s, w))


@enforce.runtime_validation
def main() -> None:
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


if __name__ == '__main__':
    main()
