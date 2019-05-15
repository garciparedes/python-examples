#!/usr/bin/env python3

import re


def super_reduced_string(s):
    r = re.sub(r'([a-z])\1', '', s)
    while r is not s:
        s = r
        r = re.sub(r'([a-z])\1', '', s)
    if not r:
        r = 'Empty String'
    return r


s = input().strip()
result = super_reduced_string(s)
print(result)
