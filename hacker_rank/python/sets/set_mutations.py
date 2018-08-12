#!/usr/bin/env python3

from typing import Iterable, List

FUNCTION_MAPPER = {
    'intersection_update': lambda s, x: s.intersection_update(x),
    'update': lambda s, x: s.update(x),
    'symmetric_difference_update': lambda s, x: s.symmetric_difference_update(x),
    'difference_update': lambda s, x: s.difference_update(x)
}


def read_line_iterator() -> List[str]:
    return input().strip().split(' ')


def read_int_line_iterator() -> Iterable[int]:
    return map(int, read_line_iterator())


def main() -> None:
    _ = int(input().strip())
    a_set = set(read_int_line_iterator())

    for _ in range(int(input().strip())):
        query, query_data_len = read_line_iterator()
        query_data = read_int_line_iterator()
        FUNCTION_MAPPER[query](a_set, query_data)

    print(sum(a_set))


if __name__ == '__main__':
    main()
