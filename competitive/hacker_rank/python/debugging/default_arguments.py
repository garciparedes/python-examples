#!/usr/bin/env python3

from abc import abstractmethod


class Stream(object):
    def __init__(self, current):
        self.current = current

    @abstractmethod
    def get_next(self) -> int:
        raise NotImplementedError


class EvenStream(Stream):
    def __init__(self):
        super().__init__(0)

    def get_next(self) -> int:
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(Stream):
    def __init__(self):
        super().__init__(1)

    def get_next(self) -> int:
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n: int, stream: Stream = None) -> None:
    if stream is None:
        stream = EvenStream()

    for _ in range(n):
        print(stream.get_next())


def main():
    queries = int(input())
    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())


if __name__ == '__main__':
    main()
