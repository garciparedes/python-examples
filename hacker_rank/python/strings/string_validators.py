#!/usr/bin/env python3

import enforce


@enforce.runtime_validation
def check_any_char(s: str, fn) -> bool:
    return any(fn(c) for c in s)


@enforce.runtime_validation
def main() -> None:
    s = input()
    print(check_any_char(s, lambda x: x.isalnum()))
    print(check_any_char(s, lambda x: x.isalpha()))
    print(check_any_char(s, lambda x: x.isdigit()))
    print(check_any_char(s, lambda x: x.islower()))
    print(check_any_char(s, lambda x: x.isupper()))


if __name__ == '__main__':
    main()
