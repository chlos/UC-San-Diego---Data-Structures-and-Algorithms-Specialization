# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_last_digit(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        res = (previous + current) % m
        previous = current
        current = res

    return res


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))

    n = 9999999999999
    m = 2
    print(get_fibonacci_last_digit(n, m))
