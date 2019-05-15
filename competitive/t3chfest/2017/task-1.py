# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def solution(N):
    b = bin(N).split('0b')[1]
    l = len(b)
    i = l / 2
    while (i > 0):
        j = 1
        while (b[0:i] == b[i * j:i * (j + 1)]):
            j += 1
            if (l == i * j):
                return i
            elif (l > i * j and l < i * (j + 1) and b[:l % i] == b[-(l % i):]):
                return i
        i -= 1
    return -1


print(solution(3))
print(solution(7))
print(solution(15))
print(solution(955))
print(solution(954))
print(solution(102))
print(solution(1000000000))
