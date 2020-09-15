# Uses python3
def calc_fib_recur(n):
    if (n <= 1):
        return n

    return calc_fib_recur(n - 1) + calc_fib_recur(n - 2)


def calc_fib(n):
    if (n <= 1):
        return n

    n0, n1 = 0, 1
    for _ in range(n - 1):
        n_fib = n0 + n1
        n0 = n1
        n1 = n_fib

    return n_fib


n = int(input())
print(calc_fib(n))
