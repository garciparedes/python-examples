#!/usr/bin/env python3

from typing import List


def read_str() -> str:
    return input().strip()


def read_int() -> int:
    return int(read_str())


def fibonacci(n: int) -> List[int]:
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[:n]


def main() -> None:
    n = read_int()
    fib_numbers = fibonacci(n)
    squared_fib_numbers = list(map(lambda x: x ** 3, fib_numbers))
    print(squared_fib_numbers)


if __name__ == '__main__':
    main()
