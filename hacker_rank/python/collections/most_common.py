#!/usr/bin/env python3

from collections import Counter


def main() -> None:
    char_counter = Counter()

    s = input().strip()
    for ch in s:
        char_counter[ch] += 1

    ordered_most_commons = sorted(char_counter.most_common(), key=lambda x: (- x[1], x[0]))

    print('\n'.join(map(lambda x: '{} {}'.format(x[0], x[1]), ordered_most_commons[:3])))


if __name__ == '__main__':
    main()
