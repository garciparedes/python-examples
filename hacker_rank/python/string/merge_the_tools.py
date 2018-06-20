#!/usr/bin/env python3

import enforce
import textwrap as tw
from collections import OrderedDict


@enforce.runtime_validation
def merge_the_tools(s: str, k: int) -> None:
    print('\n'.join(map(lambda x: ''.join(OrderedDict.fromkeys(x).keys()),
                        tw.wrap(s, k))))


@enforce.runtime_validation
def main() -> None:
    string, k = input(), int(input())
    merge_the_tools(string, k)


if __name__ == '__main__':
    main()
