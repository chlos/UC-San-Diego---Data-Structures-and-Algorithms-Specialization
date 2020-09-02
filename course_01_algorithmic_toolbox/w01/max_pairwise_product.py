# python3

import sys


def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product(numbers):
    n = len(numbers)

    max_i_1 = None
    for i in range(n):
        if max_i_1 is None or numbers[i] > numbers[max_i_1]:
            max_i_1 = i
    max_i_2 = None
    for i in range(n):
        if (max_i_2 is None or numbers[i] > numbers[max_i_2]) and i != max_i_1:
            max_i_2 = i

    max_product = numbers[max_i_1] * numbers[max_i_2]
    return max_product


def test():
    nums = [1, 2, 3]
    assert max_pairwise_product(nums) == max_pairwise_product_slow(nums)
    assert max_pairwise_product(nums) == 6

    nums = [1, 3, 2, 3]
    assert max_pairwise_product(nums) == max_pairwise_product_slow(nums)
    assert max_pairwise_product(nums) == 9

    nums = [10, 9]
    assert max_pairwise_product(nums) == max_pairwise_product_slow(nums)
    assert max_pairwise_product(nums) == 90
    nums = [9, 10]
    assert max_pairwise_product(nums) == max_pairwise_product_slow(nums)
    assert max_pairwise_product(nums) == 90

    print('OK')
    sys.exit()


if __name__ == '__main__':
    # test()

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))