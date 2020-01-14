# This code is based on "https://gist.github.com/wil3/1671fbde4c698565040a" gist.
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def regex_dist(regex: str, target: str):
    logger.info(f'Computing distance between "{regex}" and "{target}"...')

    def regex_dist_aux(r_i, t_i):
        if r_i == -1 and t_i == -1:
            return 0
        if r_i == -1:
            return t_i + 1
        if t_i == -1:
            i, counter = r_i, 0
            while i >= 0:
                char = regex[i]
                if char in ('?', '*', '+'):
                    i -= 2
                else:
                    i -= 1
                if char not in ('?', '*'):
                    counter += 1
            return counter

        if memo[r_i][t_i] is not None:
            return memo[r_i][t_i]

        # Regex special cases
        if regex[r_i] == '.':
            memo[r_i][t_i] = regex_dist_aux(r_i - 1, t_i - 1)
            return memo[r_i][t_i]

        if regex[r_i] == '+' or regex[r_i] == '*' or regex[r_i] == '?':
            if regex[r_i - 1] == target[t_i]:
                if regex[r_i] == '?':
                    memo[r_i][t_i] = regex_dist_aux(r_i - 2, t_i - 1)
                else:
                    memo[r_i][t_i] = min(regex_dist_aux(r_i - 2, t_i - 1), regex_dist_aux(r_i, t_i - 1))
            else:
                additional_cost = 1 if (regex[r_i] == '+') else 0
                memo[r_i][t_i] = min(regex_dist_aux(r_i - 2, t_i - 1) + 1,
                                     regex_dist_aux(r_i, t_i - 1) + 1,
                                     regex_dist_aux(r_i - 2, t_i) + additional_cost)
            return memo[r_i][t_i]

        # Other characters
        if regex[r_i] == target[t_i]:
            memo[r_i][t_i] = regex_dist_aux(r_i - 1, t_i - 1)
        else:
            memo[r_i][t_i] = min(regex_dist_aux(r_i - 1, t_i - 1) + 1,
                                 regex_dist_aux(r_i, t_i - 1) + 1,
                                 regex_dist_aux(r_i - 1, t_i) + 1)
        return memo[r_i][t_i]

    memo = [[None] * (len(target) + 1) for _ in range(len(regex) + 1)]
    distance = regex_dist_aux(len(regex) - 1, len(target) - 1)
    logger.info(f'The distance between "{regex}" and "{target}" is "{distance}"...')
    return distance


def main():
    # Some examples
    assert regex_dist("OrchestraaaQA+a", "CarthorseQAAAA") == 10
    assert regex_dist("A+b", "AAb") == 0
    assert regex_dist("A+b", "AAAAAb") == 0
    assert regex_dist("A+b", "AAAAAb03b") == 3
    assert regex_dist("A..b", "AAAAAb03b") == 5
    assert regex_dist("q+", "A") == 1
    assert regex_dist("q+a?a+", "A") == 2
    assert regex_dist("q+a?a+A+", "A") == 2
    assert regex_dist("q+a?a+A+.", "A") == 3
    assert regex_dist("q+A", "AAAAAb03b") == 8


if __name__ == '__main__':
    main()
