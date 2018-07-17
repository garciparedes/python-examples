#!/usr/bin/env python3

from typing import Iterable

import itertools as it
import statistics as sts


def is_in_combinations(arr, k, ch) -> Iterable[bool]:
    return map(lambda x: ch in x, it.combinations(arr, k))


def prob_to_appear_in_combinations(arr, k, ch) -> float:
    return sts.mean(is_in_combinations(arr, k, ch))


def main() -> None:
    TARGET_CH = 'a'

    _ = int(input().strip())
    arr = input().strip().split(' ')
    k = int(input().strip())

    print("{:.4f}".format(prob_to_appear_in_combinations(arr, k, TARGET_CH)))


if __name__ == '__main__':
    main()
