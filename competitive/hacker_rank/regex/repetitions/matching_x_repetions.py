#!/usr/bin/env python3

import sys
import re


def main():
    regex_pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
    print(str(bool(re.search(regex_pattern, input()))).lower())


if __name__ == '__main__':
    main()
