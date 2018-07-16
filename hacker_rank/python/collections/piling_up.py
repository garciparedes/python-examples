#!/usr/bin/env python3

from collections import deque


def get_next(cubes) -> chr:
    return cubes.pop() if cubes[0] < cubes[-1] else cubes.popleft()


def is_stackable(cubes) -> bool:
    current = get_next(cubes)
    while cubes:
        previous, current = current, get_next(cubes)
        if not (previous >= current):
            return False
    return True


def main() -> None:
    for _ in range(int(input().strip())):
        _ = input()
        cubes = deque(map(int, input().strip().split(' ')))

        print("Yes" if is_stackable(cubes) else "No")


if __name__ == '__main__':
    main()
