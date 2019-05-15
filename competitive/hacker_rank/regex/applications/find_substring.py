#!/usr/bin/env python3

import re
from typing import List

WORD_PATTERN = r'[a-zA-Z0-9_]+'


def sub_string_pattern(s: str) -> str:
    return WORD_PATTERN + s + WORD_PATTERN


def extract_words(s: str) -> List[str]:
    return list(re.findall(WORD_PATTERN, s))


def count_matches(words: List[str], query: str) -> int:
    cnt = 0
    for w in words:
        cnt += len(re.findall(sub_string_pattern(query), w))
    return cnt


def main() -> None:
    n = int(input())
    s = ""
    for i in range(n):
        s += input() + '\n'
    words = extract_words(s)
    q = int(input())
    for i in range(q):
        print(count_matches(words, input()))


if __name__ == '__main__':
    main()
