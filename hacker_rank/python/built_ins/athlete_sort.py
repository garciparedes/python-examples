#!/usr/bin/env python3

from typing import List, Iterable

import operator as op


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def read_str_line_list() -> List[str]:
    return read_str().split(' ')


def read_int_line_iterator() -> Iterable[int]:
    return map(int, read_str_line_list())


def read_int_line_list() -> List[int]:
    return list(read_int_line_iterator())


def data_table_to_str(data_table: Iterable[Iterable[int]]) -> str:
    out = str()
    for row in data_table:
        out += ' '.join(map(str, row))
        out += '\n'
    return out


def main() -> None:
    n, m = read_int_line_iterator()
    data_table = list()
    for _ in range(n):
        row = read_int_line_list()
        data_table.append(row)
    k = read_int()
    data_table.sort(key=op.itemgetter(k))
    print(data_table_to_str(data_table))


if __name__ == '__main__':
    main()
