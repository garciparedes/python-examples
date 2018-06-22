#!/usr/bin/env python3

import enforce

import cmath


@enforce.runtime_validation
def main() -> None:
    c = complex(input())
    print(abs(c))
    print(cmath.phase(c))


if __name__ == '__main__':
    main()
