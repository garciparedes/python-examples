#!/usr/bin/env python3

from typing import List


def read_str() -> str:
    return input().strip()


def read_str_list() -> List[str]:
    return read_str().split(' ')


def read_int() -> int:
    return int(read_str())


def is_vowel(letter: chr) -> int:
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def word_score(word: str) -> int:
    count = sum(map(lambda c: is_vowel(c), word))
    if count % 2:
        return 1
    else:
        return 2


def score_words(words: List[str]) -> int:
    words_score = map(word_score, words)
    return sum(words_score)


def main() -> None:
    n = read_int()
    words = read_str_list()
    print(score_words(words))


if __name__ == '__main__':
    main()
