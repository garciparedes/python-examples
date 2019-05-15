#!/usr/bin/env python3

import sys
import math


def power_sum_rec(X, l, partial_sum=0):
    count  = 0
    if partial_sum < X:
        for i in range(len(l)):
            if  partial_sum + l[i] == X:
                count += 1
            count += power_sum_rec(X, l[i+1:], partial_sum=partial_sum + l[i])
    return count


def power_sum(X, N):
    l = list(map(lambda x: x ** N, range(1, math.ceil(X ** (1 / N) + 1))))
    return power_sum_rec(X, l)


if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = power_sum(X, N)
    print(result)
