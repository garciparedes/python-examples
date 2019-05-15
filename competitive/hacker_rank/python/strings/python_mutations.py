#!/usr/bin/env python3

def mutate_string(s: str, pos: int, ch: chr) -> str:
    return s[:pos] + ch + s[pos + 1:]
    

def main() -> None:
    s = input()
    i, c = input().split()
    print(mutate_string(s, int(i), c))


if __name__ == '__main__':
    main()
