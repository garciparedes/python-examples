import math
import numpy as np


def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def weighted_euclidean_distance(a, b, w=[0.2, 0.8]):
    return math.sqrt(w[0] * (a[0] - b[0]) ** 2 + w[1] * (a[1] - b[1]) ** 2)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def hamming_distance(a, b):
    return int(a[0] != b[0]) + int(a[1] != b[1])


def distance_to_set(instance, set, function):
    result = list()
    for item in set:
        result.append(function(instance, item))
    return result

if __name__ == '__main__':
    estrellas = [
        [1, 1],
        [1, 4],
        [3, 1],
        [5, 3]
    ]

    circulos = [
        [2, 1],
        [5, 2],
        [6, 1]
    ]

    instancia = [3, 3]

    x = np.array(estrellas+circulos)

    x_normed = (x - x.min(axis=0))/ (x.max(axis=0) -x.min(axis=0))
    # print(x_normed)

    # print(estrellas)
    # print(circulos)
    # print(instancia)
    print(distance_to_set(instancia, x_normed, euclidean_distance))
    print(distance_to_set(instancia, x_normed, weighted_euclidean_distance))
    print(distance_to_set(instancia, estrellas+circulos, manhattan_distance))
    print(distance_to_set(instancia, estrellas+circulos, hamming_distance))
