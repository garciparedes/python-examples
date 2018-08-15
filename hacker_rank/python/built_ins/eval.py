#!/usr/bin/env python3


def read_str() -> str:
    return input().strip()


def eval_expression(expression: str) -> None:
    eval(expression)


def main() -> None:
    expression = read_str()
    eval_expression(expression)


if __name__ == '__main__':
    main()
