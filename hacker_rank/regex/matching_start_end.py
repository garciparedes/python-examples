#!/bin/python3

import sys
import re


def main():
    Regex_Pattern = r"^\d\w{4}\.$"
    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
