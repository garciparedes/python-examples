#!/usr/bin/env python3


def split_and_join(line: str) -> str:
    return "-".join(line.split(" "))


def main() -> None:
    print(split_and_join(input()))


if __name__ == '__main__':
    main()
