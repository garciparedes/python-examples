#!/bin/python3

import sys
import math


def unsort(comps, l=None, arr=None):
    if arr is not None:
        print(arr)
    if l is None:
        l = len(arr)
    if l == 1:
        if comps == 0:
            return [1]
        else:
            return [- 1]
    elif (comps - 1) >= l:
        arr = list(range(1, l + 1))
        print(arr)
        m_i = len(arr) // 2
        temp  = arr[m_i]
        arr[m_i] = arr[0]
        arr[0] = temp
        comps -= l - 1

        if comps > 0:
            left = unsort(comps // 2, arr=arr[:m_i])
            right = unsort(comps - comps // 2,arr=arr[(m_i + 1):])
            return left + [arr[m_i]] + right
        elif comps == 0:
            return arr
        else:
            return - 1
    else:
        return [- 1]


print(unsort(6, l=5))
#print(unsort(2, l=3))
