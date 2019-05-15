#!/usr/bin/env python3


def generate_row(i, m, middle, corner) -> str:
    return (middle * (i * 2 + 1)).center(m, corner)


def door_mat(n: int, m: int, middle=".|.", corner="-") -> str:
    s = str()
    for i in range(n // 2):
        s += generate_row(i, m, middle, corner) + '\n'
    s += "WELCOME".center(m, "-") + '\n'
    for i in reversed(range(n // 2)):
        s += generate_row(i, m, middle, corner) + '\n'
    return s


def main() -> None:
    print(door_mat(*map(int, input().strip().split())))


if __name__ == '__main__':
    main()
