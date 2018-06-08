#!/usr/bin/env python3

import sys
import re


def main():
    regex_pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
    print(str(bool(re.search(regex_pattern, input()))).lower())


if __name__ == '__main__':
    main()
