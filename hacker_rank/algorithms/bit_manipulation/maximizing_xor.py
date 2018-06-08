#!/usr/bin/env python3

import sys

def maximizingXor(l, r):
    a = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            a = max(a, i ^ j)
    return a


if __name__ == "__main__":
    l = int(input().strip())
    r = int(input().strip())
    print(l, r)
    result = maximizingXor(l, r)
    print(result)
