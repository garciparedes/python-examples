#!/usr/bin/env python3

import enforce


@enforce.runtime_validation
def generate_row(i, m, middle, corner):
    return (middle * (i * 2 + 1)).center(m, corner)


@enforce.runtime_validation
def door_mat(n: int, m: int, middle=".|.", corner="-"):
    s = str()
    for i in range(n // 2):
        s += generate_row(i, m, middle, corner) + '\n'
    s += "WELCOME".center(m, "-") + '\n'
    for i in reversed(range(n // 2)):
        s += generate_row(i, m, middle, corner) + '\n'
    return s


@enforce.runtime_validation
def main() -> None:
    print(door_mat(*map(int, input().strip().split())))


if __name__ == '__main__':
    main()
