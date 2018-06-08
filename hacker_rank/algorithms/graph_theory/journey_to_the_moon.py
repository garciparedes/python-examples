#!/usr/bin/env python3

import sys

def navigate(graph, v_i, walked=set()):
    for v_j in graph[v_i]:
        if graph.get(v_j, None) is not None:
            if len(graph[v_j]) > 0:
                walked.add(v_i)
                graph[v_j] = graph[v_j].difference(walked)
                navigate(graph, v_j, walked)
                graph[v_i] = graph[v_i].union(graph[v_j])
                graph[v_i].add(v_i)
            graph.pop(v_j)


def journey_to_moon(n, astronaut):
    sys.setrecursionlimit(max(n, sys.getrecursionlimit()))

    graph = dict()

    for edge in astronaut:
        if graph.get(edge[0], None) is None:
            graph[edge[0]] = set()
        if graph.get(edge[1], None) is None:
            graph[edge[1]] = set()
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    isolated = n - len(graph)

    for v_i in range(n):
        if graph.get(v_i, None) is not None:
            if len(graph[v_i]) > 0:
                navigate(graph,v_i)

    values = list(map(lambda x: len(x) if x != None and len(x) > 0 else 1,
                      graph.values()))
    values.sort(reverse = True)

    possibilities = 0
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            possibilities += values[i] * values[j]
        possibilities += values[i] * isolated
    possibilities += isolated * (isolated + 1) // 2 + isolated

    return possibilities


if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]
    astronaut = []
    for astronaut_i in range(p):
       astronaut_t = [int(astronaut_temp) for astronaut_temp in input().strip().split(' ')]
       astronaut.append(astronaut_t)
    result = journey_to_moon(n, astronaut)
    print(result)
