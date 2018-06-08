#!/usr/bin/env python3


def main() -> None:
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))


if __name__ == '__main__':
    main()
