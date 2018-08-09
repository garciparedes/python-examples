#!/usr/bin/env python3

import enforce


@enforce.runtime_validation
def solve(s: str) -> str:
    return s.title()


@enforce.runtime_validation
def main() -> None:
    print(solve(input()))


if __name__ == '__main__':
    main()
