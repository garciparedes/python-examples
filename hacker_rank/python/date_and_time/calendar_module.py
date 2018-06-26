#!/usr/bin/env python3

import calendar
import enforce


@enforce.runtime_validation
def get_day(month, day, year) -> str:
    return calendar.day_name[calendar.weekday(year, month, day)].upper()


@enforce.runtime_validation
def main() -> None:
    arr = list(map(int, input().split(' ')))

    print(get_day(*arr))


if __name__ == '__main__':
    main()
