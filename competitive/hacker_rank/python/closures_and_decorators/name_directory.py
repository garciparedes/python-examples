#!/usr/bin/env python3

from typing import Iterable, List, Any
import operator as op


def read_str() -> str:
    return input().strip()


def read_str_list() -> List[str]:
    return read_str().split(' ')


def read_int() -> int:
    return int(read_str())


def read_str_iterable() -> Iterable[int]:
    while True:
        yield read_str()


def normalize_person(person) -> List[Any]:
    person[-2] = int(person[-2])
    return person


def person_lister(f):
    def inner(people):
        people = map(normalize_person, people)
        people = sorted(people, key=op.itemgetter(2))
        return [f(person) for person in people]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


def main():
    people = [read_str_list() for _ in range(read_int())]
    print(*name_format(people), sep='\n')


if __name__ == '__main__':
    main()
