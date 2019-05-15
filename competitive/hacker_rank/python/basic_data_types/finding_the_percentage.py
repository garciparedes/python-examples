#!/usr/bin/env python3

import statistics as s


def main() -> None:
    arr = dict()
    for _ in range(int(input())):
        e = input().split()
        arr[e[0]] = map(float, e[1:])
    print(f'{s.mean(arr[input()]):.2f}')


if __name__ == '__main__':
    main()
