from itertools import combinations
from typing import List, Tuple, Generator


def packs(elements: List[float], bin_size: float) -> Generator[List[float], None, None]:
    elements = sorted(elements)
    for s in reversed(range(1, len(elements) + 1)):
        for group in combinations(elements, s):
            if bin_size < sum(group):
                break
            yield group


def improves_result(best: List[float], new: List[float]) -> bool:
    if len(best) < len(new):
        return True
    if len(best) == len(new) and sum(best) < sum(new):
        return True
    return False


def planificar(elements: List[float], bins: int, bin_size: float) -> List[Tuple[float]]:
    result = list()

    while elements and len(result) < bins:
        best_group = tuple()
        for group in packs(elements, bin_size):
            if not improves_result(best_group, group):
                continue
            best_group = group

            if sum(best_group) == bin_size:
                break

        result.append(best_group)
        for v in best_group:
            elements.remove(v)

    return result


def main():
    result = planificar([10, 15, 20, 5], 2, 25)
    print(result)

    mark = sum(len(group) for group in result)
    print(mark)


if __name__ == '__main__':
    main()
