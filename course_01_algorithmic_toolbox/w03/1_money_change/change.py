# Uses python3
import sys


def get_change(m):
    coins = [1, 5, 10]
    result = 0
    while m > 0:
        curr_coin = coins.pop()
        while m >= curr_coin:
            m -= curr_coin
            result += 1
    return result


def test():
    tests = [
        (1, 1), (5, 1), (10, 1),
        (2, 2), (10, 1), (20, 2),
        (6, 2), (11, 2), (15, 2),
        (16, 3),
    ]

    for m, expected in tests:
        res = get_change(m)
        print('{}: {}'.format(m, res))
        assert res == expected


if __name__ == '__main__':
    # test()  # FIXME

    m = int(sys.stdin.read())
    print(get_change(m))
