#!/bin/python3

import sys
from collections import Counter


def lonelyinteger(a):
    cnt = Counter()
    for i in a:
        cnt[i] += 1
    return cnt.most_common()[-1][0]


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
