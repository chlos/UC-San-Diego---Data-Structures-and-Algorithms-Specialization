# Uses python3
import sys


def test():
    n = 5
    res = optimal_sequence(n)
    expected = [1, 2, 4, 5]
    print(f'{n}: {res} (exp: {expected})')
    assert res == expected

    print('OK')


def optimal_sequence(n):
    min_steps_dp = get_min_steps_dp(n)
    result = get_sequence(n, min_steps_dp)
    return result


def get_min_steps_dp(n):
    steps = [0] * (n + 1)
    for i in range(2, n + 1):
        steps_add1 = steps[i - 1]
        steps_mul3 = float('inf')
        if i % 3 == 0:
            steps_mul3 = steps[i // 3]
        steps_mul2 = float('inf')
        if i % 2 == 0:
            steps_mul2 = steps[i // 2]

        steps[i] = min(steps_add1, steps_mul2, steps_mul3) + 1

    return steps


def get_sequence(n, dp):
    sequence = []
    while n:
        sequence.append(n)
        if n % 3 != 0 and n % 2 != 0:
            n -= 1
        elif n % 3 == 0 and n % 2 == 0:
            n //= 3
        elif n % 3 == 0:
            if dp[n - 1] < dp[n // 3]:
                n -= 1
            else:
                n //= 3
        elif n % 2 == 0:
            if dp[n - 1] < dp[n // 2]:
                n -= 1
            else:
                n //= 2

    sequence.reverse()
    return sequence


def optimal_sequence_greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def main():
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')


if __name__ == "__main__":
    # test()
    main()