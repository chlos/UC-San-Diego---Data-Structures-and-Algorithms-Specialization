# Uses python3
import sys


def test():
    n = 6
    res = optimal_summands(n)
    print('===== {}'.format(res))
    assert sorted(res) == sorted([1, 2, 3])

    n = 8
    res = optimal_summands(n)
    print('===== {}'.format(res))
    assert sorted(res) == sorted([1, 2, 5])

    n = 2
    res = optimal_summands(n)
    print('===== {}'.format(res))
    assert sorted(res) == sorted([2])


def optimal_summands(n):
    summands = []
    curr_summand = 0
    while n > 0 and curr_summand <= n:
        curr_summand += 1
        if n - curr_summand <= curr_summand:
            summands.append(n)
            break
        else:
            summands.append(curr_summand)
            n -= curr_summand
    return summands


def main():
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')


if __name__ == '__main__':
    # test()
    main()