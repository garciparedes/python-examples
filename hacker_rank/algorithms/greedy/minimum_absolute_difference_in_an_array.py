#!/usr/bin/env python3

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    r = abs(arr[0] - arr[1])
    for i in range(2, len(arr)):
        if abs(arr[i] - arr[i - 1]) < r:
            r = abs(arr[i] - arr[i - 1])
    return r


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
