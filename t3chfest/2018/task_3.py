#!/bin/python3


def solution(K, A):
    c = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] + A[j] == K:
                if i != j:
                    c += 2
                else:
                    c += 1
    return c


if __name__ == '__main__':
    print(solution(6, [1, 8, -3, 0, 1, 3, -2, 4, 5]))
