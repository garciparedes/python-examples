#!/usr/bin/env python3

import sys

def solve(year, programmer_day=256):
    month = 1
    day = 0
    if year == 1918 and programmer_day >= 31:
        programmer_day += 13
    while programmer_day > 0:
        if (programmer_day >= 31 and month % 2 == 1) or month == 8:
            month += 1
            programmer_day -= 31
        elif programmer_day >= 30 and month != 2 and month % 2 == 0:
            month += 1
            programmer_day -= 30
        elif month == 2 and programmer_day >= 28:
            if (programmer_day >= 29 and
                (year < 1918 and
                    year % 4 == 0) or
                (year > 1918 and
                    ((year % 4 == 0 and year % 100 != 0) or
                     year % 400 == 0))):
                month += 1
                programmer_day -= 29
            else:
                month += 1
                programmer_day -= 28
        else:
            day += programmer_day
            programmer_day = 0

    return '.'.join(map(lambda x: '0' + str(x) if x < 10 else str(x),
                        [day, month, year]))

year = int(input().strip())
result = solve(year)
print(result)
