#!/usr/bin/env python3

from collections import namedtuple
from statistics import mean


def main() -> None:
    n = int(input().strip())
    Student = namedtuple('Student', input().strip().split())

    list_students = list()
    for i in range(n):
        list_students.append(Student(*input().strip().split()))

    print('{:.2f}'.format(mean(map(lambda x: int(x.MARKS), list_students))))


if __name__ == '__main__':
    main()
