#!/usr/bin/env python3

import enforce


@enforce.runtime_validation
def solve(s: str) -> str:
    return ' '.join(map(lambda x: x.capitalize(), s.split(' ')))


@enforce.runtime_validation
def main() -> None:
    print(solve(input()))


if __name__ == '__main__':
    main()
