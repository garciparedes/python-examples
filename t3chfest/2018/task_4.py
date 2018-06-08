#!/usr/bin/env python3

def solution(A):
    sorted_A = sorted(A)
    c = 0
    i = 0
    while i < len(A):
        if A[i] != sorted_A[i]:
            j = i + 1
            while j < len(A) and A[j] != sorted_A[i]:
                j += 1
            i = j
        c += 1
        i += 1
    return c



if __name__ == '__main__':
    print(solution([1, 5, 4, 9, 8, 7, 12, 13, 14]))
    print(solution([4, 3, 2, 6, 1]))
    print(solution([2, 1, 3]))
