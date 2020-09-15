# Uses python3
import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm(a, b):
    return int((a * b) / gcd(a, b))


if __name__ == '__main__':
    # import time
    # N = 100

    # ts_start = time.time()
    # f = lcm_naive
    # for a in range(1, N):
    #     for b in range(1, N):
    #         f(a, b)
    # print('{} {}'.format(f, time.time() - ts_start))   # FIXME

    # ts_start = time.time()
    # f = lcm
    # for a in range(1, N):
    #     for b in range(1, N):
    #         f(a, b)
    # print('{} {}'.format(f, time.time() - ts_start))   # FIXME

    # for a in range(1, N):
    #     for b in range(1, N):
    #         assert lcm_naive(a, b) == lcm(a, b)
    # print('Tests OK: {} {}'.format(lcm, time.time() - ts_start))   # FIXME

    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm(a, b))