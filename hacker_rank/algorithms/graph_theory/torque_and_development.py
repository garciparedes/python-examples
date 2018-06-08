#!/usr/bin/env python3

import sys

from collections import deque, OrderedDict


def navigate(graph, v_i, cost, queue=None):
    actual_cost = 0
    covered = 0
    if graph.get(v_i, None) is not None:
        covered += 1
        l = graph[v_i]
        graph.pop(v_i)

        if queue == None:
            queue = l
        else:
            queue.extend(l)
            actual_cost += cost
        for i in range(len(l)):
            [covered1, actual_cost1] = navigate(graph, queue.pop(), cost, queue)
            covered += covered1
            actual_cost += actual_cost1
    return [covered, actual_cost]


def roadsAndLibraries(n, c_lib, c_road, cities):
    cost = 0
    if c_road < c_lib and len(cities) > 0:
        graph = { k: deque() for k in range(1, n + 1) }
        for edge in cities:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        graph = OrderedDict(sorted(graph.items(), key = lambda t: t[1]))
        covered = 0
        for v_i in range(1, n + 1):
            if len(graph[v_i]) == 0:
                cost += c_lib
                covered += 1
                graph.pop(v_i)
        while covered < n:
            [covered1, cost1] = navigate(graph, next(iter(graph)), c_road)
            cost += cost1 + c_lib
            covered += covered1
    else:
        cost += c_lib * n
    return cost


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
            cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
            cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
