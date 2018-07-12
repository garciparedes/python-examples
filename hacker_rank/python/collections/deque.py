#!/usr/bin/env python3

from collections import deque


def main() -> None:
    s = deque()

    operations = {
        'append': lambda s, x: s.append(x),
        'appendleft': lambda s, x: s.appendleft(x),
        'pop': lambda s: s.pop(),
        'popleft': lambda s: s.popleft()
    }

    for _ in range(int(input().strip())):
        query = input().strip().split()
        operations[query[0]](s, *map(int, query[1:]))

    print(' '.join(map(str, s)))


if __name__ == '__main__':
    main()
