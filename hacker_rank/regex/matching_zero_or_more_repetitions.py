#!/bin/python3

import sys
import re


def main():
    regex_pattern = r'^\d{2,}[a-z]*[A-Z]*$'
    print(str(bool(re.search(regex_pattern, input()))).lower())


if __name__ == '__main__':
    main()