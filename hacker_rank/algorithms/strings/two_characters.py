#!/usr/bin/env python3

import sys
import re


def check_correct(r):
    l = len(r)
    correct = True
    k = 1
    while k < l:
        if r[k - 1] == r[k]:
            correct = False
        k += 1
    return correct

def two_charaters(s):
    distinct = set()
    for c in s:
        distinct.add(c)
    distinct_list = list(distinct)
    dictinct_len = len(distinct_list)
    max_len = 0
    for i in range(dictinct_len):
        for j in range(i + 1, dictinct_len):
            r = re.sub('[^(' + distinct_list[i] + distinct_list[j] +')]','', s)
            if check_correct(r) == True:
                max_len = max(max_len, len(r))
    return max_len


if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = two_charaters(s)
    print(result)
