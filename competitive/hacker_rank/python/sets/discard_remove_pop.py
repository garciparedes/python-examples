#!/usr/bin/env python3

FUNCTION_MAPPER = {
    'pop': lambda s: s.pop(),
    'remove': lambda s, x: s.remove(x),
    'discard': lambda s, x: s.discard(x)
}

def read_int_line_iterator():
    return frozenset(map(int, input().strip().split()))

def main() -> None:
    _ = input()
    s = set(map(int, input().strip().split(' ')))

    for _ in range(int(input().strip())):
        query = input().strip().split()
        FUNCTION_MAPPER[query[0]](s, *map(int, query[1:]))

    print(sum(s))


if __name__ == '__main__':
    main()
