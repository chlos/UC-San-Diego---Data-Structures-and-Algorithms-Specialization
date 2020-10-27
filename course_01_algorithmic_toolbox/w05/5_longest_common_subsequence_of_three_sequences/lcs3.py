#!/usr/bin/env python3

import sys


def test():
    a = [1, 2, 3]
    b = [2, 1, 3]
    c = [1, 3, 5]
    res = lcs3(a, b, c)
    exp = 2
    print(f'lcs2({a}, {b}, {c}) = {res} (expected: {exp})')
    assert res == exp

    a = [8, 3, 2, 1, 7]
    b = [8, 2, 1, 3, 8, 10, 7]
    c = [6, 8, 3, 1, 4, 7]
    res = lcs3(a, b, c)
    exp = 3
    print(f'lcs2({a}, {b}, {c}) = {res} (expected: {exp})')
    assert res == exp

    print('OK')


def lcs3(a, b, c):
    dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                else:
                    dp[i][j][k] = max(
                        dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1]
                    )

    return dp[len(a)][len(b)][len(c)]


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))


if __name__ == '__main__':
    # test()
    main()