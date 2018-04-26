#!/bin/python3

import sys
import re


def main():
    Regex_Pattern = r".{3}\W.{10}\W.{3}"
    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
