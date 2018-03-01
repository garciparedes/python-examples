#!/bin/python3

def swap(S, T):
    for i in range(len(T) - 1):
        if (S[i] == T[i + 1] and S[i + 1] == T[i] and
            S[i] != T[i] and S[i + 1] != T[i + 1]):
            if S[i + 2:] == T[i + 2:]:
                return "SWAP " + S[i] + " " + S[i + 1]
            else:
                return "IMPOSSIBLE"


def insertion(A, B, action):
    for i in range(len(B)):
        if i == len(A) or A[i] != B[i]:
            if A[i:] == B[i+1:]:
                return action + " " + B[i]
            else:
                return "IMPOSSIBLE"


def solution(S, T):
    diff = len(S) - len(T)
    if diff == 1:
        return insertion(T, S, "DELETE")
    elif diff == - 1:
        return insertion(S, T, "INSERT")
    elif diff == 0:
        if S == T:
            return "NOTHING"
        else:
            return swap(S, T)
    else:
        return "IMPOSSIBLE"


if __name__ == '__main__':
    print(solution("inces","nicse"))
