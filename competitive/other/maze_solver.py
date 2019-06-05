from itertools import chain
from typing import Tuple, Sequence, List, Set

Path = Sequence[Tuple[int, int]]


def maze_solver(edges: Set[Tuple[int, int]], start: int, path: Path = tuple()) -> Path:
    if 0 in chain(*path):
        return path

    best_path = None
    for edge in set(edge for edge in edges if start in edge):

        current_start = edge[0] if edge[1] == start else edge[1]
        current_edges = set(edge for edge in edges if edge not in path)
        current_path = (*path, edge)

        new_path = maze_solver(current_edges, current_start, current_path)

        if new_path is None:
            continue
        if 0 not in chain(*new_path):
            continue
        if best_path is not None and not len(new_path) < len(best_path):
            continue

        best_path = new_path

    return best_path


def main() -> None:
    graph = {
        (0, 1),
        (1, 2),
        (2, 3),
        (1, 3),
    }

    solution = maze_solver(graph, 3)
    print(solution)


if __name__ == '__main__':
    main()
