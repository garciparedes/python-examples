#!/bin/python3

bit = lambda x: x % 2
carry = lambda x: 1 if x < 0 else -1 if x > 1 else 0

def solution(A):
    R = []
    if len(A) > 0:
        R.append(bit(A[0]))
        c = carry(A[0])
        for i in range(1, len(A)):
            n = A[i] + A[i - 1] + c
            R.append(bit(n))
            c = carry(n)
        n = A[-1] + c
        R.append(bit(n))
        while len(R) > 0 and R[-1] == 0:
            R.pop()
    return R


if __name__ == '__main__':
    print(solution([0]))
