# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import numpy as np

def solution(A, D):
    # write your code in Python 2.7
    season = 0
    M = [False for col in range(len(A))]

    iterator = A[0:D]
    while(season < len(A)):
        for i, a in enumerate(iterator):
            if (a >= 0 and a <= season):
                M[i] = True
                if len(iterator) < len(A):
                    iterator.extend(range(i,i+D))
                    pass
        print((M))
        j = D
        while (j > 0):
            if(M[-j]):
                return season
            j -= 1
        season += 1


    return -1


print(solution([1, -1, 0, 2, 3, 5], 3))
print(solution([3, 2, 1], 1))
print(solution([1, 2, 3, 4, -1, -1, -1], 3))
