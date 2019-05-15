#!/usr/bin/env python3


from typing import Iterable, List, Any

import re

REGEX = re.compile(r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9])+(?=[a-zA-Z0-9])')


def read_str() -> str:
    return input()


def read_str_list() -> List[str]:
    return read_str().split(' ')


def read_int() -> int:
    return int(read_str())


def read_int_iterable() -> Iterable[int]:
    return map(int, read_str_list())


def rotate_matrix(matrix: List[List[Any]]) -> List[List[Any]]:
    return list(zip(*matrix))


def matrix_to_str(matrix_str: List[List[str]]) -> str:
    return ''.join(''.join(row) for row in matrix_str)


def decode(matrix_str: List[List[str]]):
    matrix_str = rotate_matrix(matrix_str)
    text = matrix_to_str(matrix_str)

    text = re.sub(REGEX, ' ', text)
    return text


def main() -> None:
    rows, columns = read_int_iterable()
    matrix_str = list()
    for i in range(rows):
        row_str = '{:{width}s}'.format(read_str(), width=columns)
        matrix_str.append(row_str)
    text = decode(matrix_str)
    print(text)


if __name__ == '__main__':
    main()
