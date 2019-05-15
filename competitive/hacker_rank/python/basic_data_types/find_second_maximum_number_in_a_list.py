#!/usr/bin/env python3

from typing import Iterator


def runner_up(arr: Iterator[int]) -> int:
    return sorted(set(arr))[-2]


def main() -> None:
    _ = int(input())
    arr = map(int, input().split())
    print(runner_up(arr))


if __name__ == '__main__':
    main()
