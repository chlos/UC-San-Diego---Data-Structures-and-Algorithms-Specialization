# Uses python3


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_1(n):
    # if n <= 1:
    #     return n

    previous = 0
    current = 1

    n = (n + 2) % 60
    for _ in range(n):
        previous, current = current, (previous + current) % 10

    return 9 if previous == 0 else previous - 1


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        res = (previous + current) % 10
        previous = current
        current = res

    return res


if __name__ == '__main__':
    assert get_fibonacci_last_digit(2) == 1
    assert get_fibonacci_last_digit(240) == 0

    n = int(input())
    # n = 100  # FIXME
    # n = 999999 # FIXME
    print(get_fibonacci_last_digit(n))