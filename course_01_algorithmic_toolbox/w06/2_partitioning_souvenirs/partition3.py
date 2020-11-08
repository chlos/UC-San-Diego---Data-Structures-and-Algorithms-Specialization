# Uses python3
import sys
import itertools

K = 3


def test():
    a = [3, 3, 3, 3]
    res = partition3(a)
    print(f'{a}: {res}')
    assert res == False

    a = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    res = partition3(a)
    print(f'{a}: {res}')
    assert res == True

    print('OK')


def partition3_bruteforce(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3(A):
    if len(A) < K or sum(A) % K:
        return 0

    third = sum(A) // K
    dp = [[0] * (len(A) + 1) for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(A) + 1):
            ii = i - A[j - 1]
            if A[j - 1] == i or (ii > 0 and dp[ii][j - 1]):
                dp[i][j] = 1 if dp[i][j - 1] == 0 else 2
            else:
                dp[i][j] = dp[i][j - 1]

    if dp[-1][-1] == 2:
        return 1
    else:
        return 0


def main():
    input = sys.stdin.read()
    _, *A = list(map(int, input.split()))
    print(partition3(A))


if __name__ == '__main__':
    # test()
    main()