#!/usr/bin/env python3


def main() -> None:
    n = int(input())
    print(str().join(map(str, range(1, n + 1))))


if __name__ == '__main__':
    main()
