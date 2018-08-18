#!/usr/bin/env python3

from typing import List, Iterable


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


def is_positive(number: int) -> bool:
    return number > 0


def is_palindromic(number: int) -> bool:
    text_number = str(number)
    i = 0
    j = len(text_number) - 1
    while i < j and text_number[i] == text_number[j]:
        i += 1
        j -= 1

    return i >= j


def main() -> None:
    _ = read_int()
    numbers = read_int_line_list()
    result = all(map(is_positive, numbers))
    result &= any(map(is_palindromic, numbers))
    print(result)


if __name__ == '__main__':
    main()
