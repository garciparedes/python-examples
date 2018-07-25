#!/usr/bin/env python3

import itertools as it


def maximize(k_list, m):
    max_value = 0
    for configuration in it.product(*k_list):
        max_value = max(max_value, sum(configuration) % m)
    return max_value


def main() -> None:
    k, m = map(int, input().strip().split(' '))

    k_list = list()
    for _ in range(k):
        l_raw = input().strip().split(' ')[1:] # To ignore the count element
        l_squared = map(lambda x: int(x) ** 2, l_raw)
        k_list.append(l_squared)

    print(maximize(k_list, m))


if __name__ == '__main__':
    main()
