#!/usr/bin/env python3

import re


def process(op: str, l: list) -> list:
    regex = re.match(re.compile(r"""(?P<insert>insert\s(?P<insert_i>\d+)\s(?P<insert_e>\d+))|
                                        (?P<print>print)|
                                        (?P<remove>remove\s(?P<remove_e>\d+))|
                                        (?P<append>append\s(?P<append_e>\d+))|
                                        (?P<sort>sort)|
                                        (?P<pop>pop)|
                                        (?P<reverse>reverse)""", re.X), op)
    if regex.group('insert') is not None:
        l.insert(int(regex.group('insert_i')), int(regex.group('insert_e')))
    elif regex.group('print') is not None:
        print(l)
    elif regex.group('remove') is not None:
        l.remove(int(regex.group('remove_e')))
    elif regex.group('append') is not None:
        l.append(int(regex.group('append_e')))
    elif regex.group('sort') is not None:
        l.sort()
    elif regex.group('pop') is not None:
        l.pop()
    elif regex.group('reverse') is not None:
        l.reverse()
    return l


def main() -> None:
    N = int(input())
    l = list()
    for op in range(N):
        l = process(input(), l)


if __name__ == '__main__':
    main()
