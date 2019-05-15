#!/usr/bin/env python3

from typing import List, Iterable


def read_str_line_list() -> List[str]:
    return input().strip().split(' ')


def read_int_line_iterator() -> Iterable[int]:
    return map(int, read_str_line_list())


def read_float_line_iterator() -> Iterable[float]:
    return map(float, read_str_line_list())


def read_float_zipped_block_iterator(lines: int) -> Iterable[Iterable[float]]:
    return zip(*(read_float_line_iterator() for _ in range(lines)))


def iterable_mean(data: Iterable[float]) -> float:
    return sum(data) / len(data)


def table_mean_by_row(data: Iterable[Iterable[float]]) -> Iterable[float]:
    return map(iterable_mean, data)


def float_iterable_to_str(data: Iterable[float], decimals=1) -> str:
    return '\n'.join(map(lambda x: '{:.1f}'.format(x), data))


def main() -> None:
    n, x = read_int_line_iterator()
    data = read_float_zipped_block_iterator(x)
    result = table_mean_by_row(data)
    print(float_iterable_to_str(result))


if __name__ == '__main__':
    main()
