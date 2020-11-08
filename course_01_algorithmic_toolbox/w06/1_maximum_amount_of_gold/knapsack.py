#!/usr/bin/env python3

import sys


def test():
    W = 10
    w = [1, 4, 8]
    res = optimal_weight(W, w)
    exp = 9
    print(f'res: {res}; exp: {exp}')
    assert res == exp
    print('OK')


def optimal_weight_greedy(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight(W, w):
    n = len(w)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for curr_weight in range(1, W + 1):
            # use previous optimal sub-solution
            dp[i][curr_weight] = dp[i - 1][curr_weight]
            if w[i - 1] <= curr_weight:
                curr_value = dp[i - 1][curr_weight - w[i - 1]] + w[i - 1]
                if curr_value > dp[i][curr_weight]:
                    dp[i][curr_weight] = curr_value

    return dp[n][W]


def main():
    input = sys.stdin.read()
    W, _, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


if __name__ == '__main__':
    # test()
    main()