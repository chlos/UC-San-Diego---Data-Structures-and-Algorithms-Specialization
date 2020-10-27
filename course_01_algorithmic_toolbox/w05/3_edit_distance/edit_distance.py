#!/usr/bin/env python3


def test():
    s1 = 'ab'
    s2 = 'ab'
    result = edit_distance(s1, s2)
    expected = 0
    print(f'{s1} {s2} dist: {result} (expected: {expected}')
    assert result == expected

    s1 = 'short'
    s2 = 'ports'
    result = edit_distance(s1, s2)
    expected = 3
    print(f'{s1} {s2} dist: {result} (expected: {expected}')
    assert result == expected

    s1 = 'editing'
    s2 = 'distance'
    result = edit_distance(s1, s2)
    expected = 5
    print(f'{s1} {s2} dist: {result} (expected: {expected}')
    assert result == expected

    print('OK')


def edit_distance(s, t):
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
    for i in range(len(t) + 1):
        for j in range(len(s) + 1):

            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i

            elif t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1],
                )

    return dp[len(t)][len(s)]


def main():
    print(edit_distance(input(), input()))


if __name__ == "__main__":
    # test()
    main()