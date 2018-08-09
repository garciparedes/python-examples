#!/usr/bin/env python3


def main() -> None:

    for _ in range(int(input())):
        a, b = input().strip().split()

        try:
            print(int(a) // int(b))
        except (ZeroDivisionError, ValueError) as e:
            print('Error Code: {}'.format(e))


if __name__ == '__main__':
    main()
