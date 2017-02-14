# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(T):
    c = find_capital(T)
    Graph = list(enumerate(T));
    Distances = [0] * (len(T) - 1)

    deep = 0
    Graph.pop(c)
    Queue = [c]
    while (len(Queue) != 0):

        if (Queue[0] != -1):
            Queue.append(-1)

        for road in list(Graph):
            if (Queue[0] == road[1]):
                Distances[deep] += 1
                Queue.append(road[0])
                Graph.remove(road)

        if (Queue.pop(0) == -1):
            deep += 1
    return Distances


def find_capital(T):
    for deep, j in enumerate(T):
        if (deep == j):
            return deep


print(solution([9, 1, 4, 9, 0, 4, 8, 9, 0, 1]))
