#!/usr/bin/env python3

import sys


def insertionSort1(n, arr):
    elem = arr[n - 1]
    i = n
    shifted = True
    while 0 < i and shifted:
        shifted = False
        i -= 1
        if i and elem < arr[i - 1]:
            arr[i] = arr[i - 1]
            shifted = True
        else:
            arr[i] = elem
    return arr


def insertionSort2(n, arr):
    for i in range(2, n + 1):
        arr[:i] = insertionSort1(i, arr[:i])
        print(' '.join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
