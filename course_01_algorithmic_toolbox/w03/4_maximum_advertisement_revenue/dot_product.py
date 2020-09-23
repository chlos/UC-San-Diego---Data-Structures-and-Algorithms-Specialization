# Uses python3

import sys


def test():
    cpc = [1, 3, -5]
    ctr = [-2, 4, 1]
    res = max_dot_product(cpc, ctr)
    print('===== {}'.format(res))
    assert res == 23


def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    # test()

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))