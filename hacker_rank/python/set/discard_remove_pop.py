#!/usr/bin/env python3


def main() -> None:
    _ = input()
    s = set(map(int, input().strip().split(' ')))

    operations = {
        'pop': lambda s: s.pop(),
        'remove': lambda s, x: s.remove(x),
        'discard': lambda s, x: s.discard(x)
    }

    for _ in range(int(input().strip())):
        query = input().strip().split()
        operations[query[0]](s, *map(int, query[1:]))

    print(sum(s))


if __name__ == '__main__':
    main()
