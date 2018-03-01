#!/bin/python3

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
    return graph

def merge_graph(graph1, graph2):
    if len(graph1) < len(graph2):
        temp = graph1
        graph1 = graph2
        graph2 = temp

    graph1 = dict(graph1)
    for v_i, v in graph2.items():
        if graph1.get(v_i, None) is None:
            graph1[v_i] = v
        else:
            graph1[v_i] = graph1[v_i].union(v)
        for v_j in v:
            if graph1.get(v_j, None) is None:
                graph1[v_j] = set([v_i])
            else:
                graph1[v_j].add(v_i)
    return graph1

def get_edges(number):
    v = []
    for i, bit in enumerate(reversed(bin(number)[2:])):
        if bit == '1':
            v.append(i)
    edges = []
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            edges.append([v[i], v[j]])
    return edges

def subset_component(d):
    n = 64

    total = n

    graph = [dict() for i in range(len(d))]
    for i in range(len(d)):
        edges = get_edges(d[i])
        for edge in edges:
            if graph[i].get(edge[0], None) is None:
                graph[i][edge[0]] = set()
            if graph[i].get(edge[1], None) is None:
                graph[i][edge[1]] = set()
            graph[i][edge[0]].add(edge[1])
            graph[i][edge[1]].add(edge[0])
    #print((navigate(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(merge_graph(graph[0], graph[1]), graph[2]), graph[3]), graph[4]), graph[5]), graph[6]), graph[7]), graph[8]), graph[9]), graph[10]), graph[11]), graph[12]), graph[13]), graph[14]), graph[15]), graph[16]), graph[17]), graph[18]), graph[19]), 0)))

if __name__ == "__main__":


    input_data = iter("""20
                         49834558446328399 5130453145419639095 3425104317966070419 8269211681151561749 9020013969337412448 1967495374752297648 1745468902913229067 9110028150128674329 697752326988056756 6936011071386985190 6325678747542723457 5118412050199196005 4458581988620336246 8276875575632510920 4211098577587333379 4358018573821037917 1790989491150673991 9011658438688069111 9094338560997420735 2635782602074303149
                         """.splitlines())
    input = lambda: next(input_data)
    n = int(input().strip())
    d = list(map(int, input().strip().split(' ')))
    result = subset_component(d)
    print(result)
