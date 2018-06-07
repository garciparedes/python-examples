#!/bin/python3

from typing import List, Tuple

import enforce


@enforce.runtime_validation
def runner_up(arr: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    arr.sort(key=lambda x: x[1])
    i = 0
    min_value = arr[i][1]
    while arr[i][1] == min_value:
        i += 1
    target_value = arr[i][1]
    j = i
    while j < len(arr) and arr[j][1] == target_value:
        j += 1
    return sorted(arr[i:j], key=lambda x: x[0])


@enforce.runtime_validation
def main() -> None:
    arr = list()
    for _ in range(int(input())):
        arr.append((input(), float(input())))
    print('\n'.join(map(lambda x: x[0], runner_up(arr))))


if __name__ == '__main__':
    main()
