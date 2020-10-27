#!/usr/bin/env python3

import sys

COINS = [1, 3, 4]


def test():
    money = 34
    result = get_change(money, COINS)
    expected = 9
    print(f'money: {money}; result: {result}; expected: {expected}')
    assert result == expected

    print('OK')


def get_change(money, coins):
    min_coins_dp = [None] * (money + 1)
    min_coins_dp[0] = 0
    for curr_money in range(1, money + 1):
        min_coins_dp[curr_money] = float('inf')
        for coin in coins:
            if coin <= curr_money:
                curr_num_coins = min_coins_dp[curr_money - coin] + 1
                if curr_num_coins < min_coins_dp[curr_money]:
                    min_coins_dp[curr_money] = curr_num_coins

    return min_coins_dp[money]


def main():
    m = int(sys.stdin.read())
    print(get_change(m, COINS))


if __name__ == '__main__':
    # test()
    main()