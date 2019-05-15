#!/usr/bin/env python3

VOWEL_LETTERS = ['A', 'E', 'I', 'O', 'U']


def calculate_scores(game_string: str) -> int:
    kevin_score = 0
    stuart_score = 0

    for i in range(len(game_string)):
        step_score = len(game_string) - i
        if game_string[i] in VOWEL_LETTERS:
            kevin_score += step_score
        else:
            stuart_score += step_score

    return kevin_score, stuart_score


def calculate_winner(game_string: str) -> int:

    kevin_score, stuart_score = calculate_scores(game_string)

    if stuart_score == kevin_score:
        return 'Draw'
    elif stuart_score > kevin_score:
        return 'Stuart {}'.format(stuart_score)
    else:
        return 'Kevin {}'.format(kevin_score)


def main() -> None:
    game_string = input().strip()
    result = calculate_winner(game_string)
    print(result)


if __name__ == '__main__':
    main()
