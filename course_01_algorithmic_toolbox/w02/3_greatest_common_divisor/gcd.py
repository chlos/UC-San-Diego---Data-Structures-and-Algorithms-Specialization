# Uses python3
import sys
# import time


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclidean_recur(a, b):
    a, b = max(a, b), min(a, b)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd_euclidean_recur(r, b)


def gcd_euclidean_iter(a, b):
    a, b = max(a, b), min(a, b)
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


if __name__ == "__main__":
    # ts_start = time.time()
    # for a in range(1, 1000):
    #     for b in range(1, 1000):
    #         assert gcd_euclidean_iter(a, b) == gcd_naive(a, b)
    # print('Tests OK: {} {}'.format(gcd_euclidean_iter, time.time() - ts_start))   # FIXME

    # ts_start = time.time()
    # for a in range(1, 1000):
    #     for b in range(1, 1000):
    #         assert gcd_euclidean_recur(a, b) == gcd_naive(a, b)
    # print('Tests OK: {} {}'.format(gcd_euclidean_recur, time.time() - ts_start))   # FIXME

    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd_euclidean_iter(a, b))