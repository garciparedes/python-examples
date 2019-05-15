#!/usr/bin/env python3


def magic_expression(i) -> int:
    return (10 ** i - 1) ** 2 // 81  # Magic Expression


def main() -> None:
    n = int(input().strip())
    for i in range(1, n + 1):
        value = magic_expression(i)
        print(value)


if __name__ == '__main__':
    main()
