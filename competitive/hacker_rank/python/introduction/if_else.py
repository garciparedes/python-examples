#!/usr/bin/env python3


def is_weird(n: int) -> bool:
    if n % 2 is 1:
        return True
    else:
        if 2 <= n <= 5:
            return False
        elif 6 <= n <= 20:
            return True
        else:
            return False


def main() -> None:
    n = int(input())
    if is_weird(n):
        print("Weird")
    else:
        print("Not Weird")


if __name__ == '__main__':
    main()
