#!/usr/bin/env python3

def solution(A):
    c = 0
    i = 0
    while i < len(A) - 1:
        if A[i] > A[i + 1]:

            j = i - 1
            while j >= 0 and A[j] > A[i + 1] and not A[j] > A[j + 1]:
                j -= 1
            l = i - j

            j = i + 1
            while j < len(A) and A[j] < A[i] and j - (i + 1) < l:
                j += 1
            r =  j - (i + 1)

            if r < l:
                i += r
                c += r
            else:
                c+=l

        i += 1
    return c



if __name__ == '__main__':
    print(solution([1,2,3,4,5,6,7,5,6,7,8,10,10,10,10,10,10,10,10,10,10,9,1, 11,2]))
