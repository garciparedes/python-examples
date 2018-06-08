#!/usr/bin/env python3

def check_vector(A):
    parity = A[0] % 2
    for i in range(1, len(A)):
        if A[i] % 2 != parity:
            return False
    return True

def equal_vector(A):
    for i in range(len(A) - 1):
        if A[i] != A[i + 1]:
            return False
    return True


def solution(A):
    if len(A) == 0:
        return 0
    elif check_vector(A):
        count = 0
        matched = equal_vector(A)
        while not matched:
            count += 1
            mean = (sum(A) / len(A))
            for i in range(len(A)):
                if A[i] - mean < 0:
                    A[i] += 1
                else:
                    A[i] -= 1
            matched = equal_vector(A)
        return count
    else:
         return -1

if __name__ == '__main__':
    print(solution([200, -200, 10, 2]))
