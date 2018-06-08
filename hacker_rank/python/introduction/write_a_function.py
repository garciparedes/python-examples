#!/usr/bin/env python3


def is_leap(year: int) -> bool:
    return not (bool(year % 4)) and bool(year % 100) or not (bool(year % 400))


def main() -> None:
    year = int(input())
    print(is_leap(year))


if __name__ == '__main__':
    main()
