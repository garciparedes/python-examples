#!/usr/bin/env python3

from collections import Counter


def lonely_integer(a):
    cnt = Counter()
    for i in a:
        cnt[i] += 1
    return cnt.most_common()[-1][0]


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonely_integer(a)
print(result)
