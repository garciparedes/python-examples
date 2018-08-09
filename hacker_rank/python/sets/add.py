#!/usr/bin/env python3


def main() -> None:
    s = set()
    for _ in range(int(input().strip())):
        s.add(input().strip())
    print(len(s))


if __name__ == '__main__':
    main()
