# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import time


def solution(A):
    # write your code in Python 2.7
    result = 0
    data = dict()
    for a in A:
        if not a in data:
            d = 2 ** a
            if a % 2 == 1:
                d *= -1
            data[(a)] = d
        result += data[a]
    return result


time1 = time.time()
(solution([1000000, 999999, 999998, 999998, 7]))
time2 = time.time()
print('took %0.3f ms' % ((time2 - time1) * 1000.0))

time1 = time.time()
(solution([1000000, 1000000, 1000000, 7]))
time2 = time.time()
print('took %0.3f ms' % ((time2 - time1) * 1000.0))
