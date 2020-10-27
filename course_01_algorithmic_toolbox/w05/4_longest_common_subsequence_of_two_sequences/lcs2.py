#!/usr/bin/env python3

import sys


def test():
    a = [2, 7, 5]
    b = [2, 5]
    res = lcs2(a, b)
    exp = 2
    print(f'lcs2({a}, {b}) = {res} (expected: {exp})')
    assert res == exp

    a = [7]
    b = [1, 2, 3, 4]
    res = lcs2(a, b)
    exp = 0
    print(f'lcs2({a}, {b}) = {res} (expected: {exp})')
    assert res == exp

    a = [2, 7, 8, 3]
    b = [5, 2, 8, 7]
    res = lcs2(a, b)
    exp = 2
    print(f'lcs2({a}, {b}) = {res} (expected: {exp})')
    assert res == exp

    print('OK')


def lcs2(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i][j - 1]
                )

    return dp[len(a)][len(b)]


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))


if __name__ == '__main__':
    # test()
    main()