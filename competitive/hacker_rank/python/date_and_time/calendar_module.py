#!/usr/bin/env python3

import calendar


def get_day(month, day, year) -> str:
    return calendar.day_name[calendar.weekday(year, month, day)].upper()


def main() -> None:
    arr = list(map(int, input().split(' ')))

    print(get_day(*arr))


if __name__ == '__main__':
    main()
