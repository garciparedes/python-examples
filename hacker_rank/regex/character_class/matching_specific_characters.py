#!/usr/bin/env python3

import sys
import re


def main():
    regex_pattern = r'^[123][012][sx0][03aA][usxs][\.,]$'
    print(str(bool(re.search(regex_pattern, input()))).lower())


if __name__ == '__main__':
    main()
