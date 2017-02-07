# you can write to stdout for debugging purposes, e.g.
# print 'this is a debug message'

def solution(A, B):
    resultList, remainderList = [str(A//B)], [A % B]
    A %= B
    stop = False
    while A != 0 and not stop:
        quotient, A = divmod(A * 10, B)
        resultList.append(str(quotient))
        if A in remainderList:
            resultList.insert(remainderList.index(A) + 1, '(')
            resultList.append(')')
            stop = True
        else:
            remainderList.append(A)
    if (len(resultList) == 1):
        return resultList[0]
    else:
        resultList.insert(1, '.')
        return ''.join(resultList)


print(solution(12,3))
print(solution(1,2))
print(solution(5,4))
print(solution(1,3))
print(solution(3,28))
