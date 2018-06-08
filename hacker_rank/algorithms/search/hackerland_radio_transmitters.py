#!/usr/bin/env python3

import sys


def position_finder(x, k, i):
    fixed_t = False
    j = 0
    while not fixed_t:
        if x[i] + k - j in x[i:i + k + 1]:
            fixed_t = True
            last_t = x[i] + k - j
        else:
            j += 1
    return last_t


def hackerlandRadioTransmitters(x, k):
    x = sorted(set(x))
    last_t = position_finder(x, k, 0)
    cnt = 1
    for i in range(1, len(x)):
        if abs(x[i] - last_t) > k:
            last_t = position_finder(x, k, i)
            cnt += 1
    return cnt


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    x = list(map(int, input().strip().split(' ')))
    result = hackerlandRadioTransmitters(x, k)
    print(result)
