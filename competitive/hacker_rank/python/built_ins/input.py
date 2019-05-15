#!/usr/bin/env python3

from typing import List, Iterable


def read_str() -> str:
    return input().strip()


def read_str_line_list() -> List[str]:
    return read_str().split(' ')


def read_int_line_iterator() -> Iterable[int]:
    return map(int, read_str_line_list())


def eval_polynomial(expression: str, x: int) -> int:
    return eval(expression)


def main() -> None:
    x, k = read_int_line_iterator()
    expression = read_str()
    result = eval_polynomial(expression, x)
    print(result == k)


if __name__ == '__main__':
    main()
