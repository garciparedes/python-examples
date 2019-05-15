#!/usr/bin/env python3

from collections import Counter


def calculate_happiness(cnt_arr, set_a, set_b) -> int:
    happiness = 0
    for v, n in cnt_arr.most_common():
        if v in set_a:
            happiness += n
        elif v in set_b:
            happiness -= n
    return happiness


def main() -> None:
    n, m = map(int, input().strip().split())
    cnt_arr = Counter(input().strip().split())
    set_a = frozenset(input().strip().split())
    set_b = frozenset(input().strip().split())
    # assert(n == len(cnt_arr) and m == len(set_a) and m == len(set_b))

    print(calculate_happiness(cnt_arr, set_a, set_b))


if __name__ == '__main__':
    main()
