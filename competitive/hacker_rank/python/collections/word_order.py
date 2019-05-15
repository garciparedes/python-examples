#!/usr/bin/env python3

from collections import OrderedDict


def main() -> None:
    word_counter = OrderedDict()

    for _ in range(int(input().strip())):
        s = input().strip()
        if s not in word_counter:
            word_counter[s] = 0
        word_counter[s] += 1

    print(len(word_counter))
    print(' '.join(map(str, word_counter.values())))


if __name__ == '__main__':
    main()
