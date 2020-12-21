# python3


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def get_left_child_i(i):
    return int(2 * (i + 1) - 1)


def get_right_child_i(i):
    return int(2 * (i + 1))


def sift_down(data, i, swaps):
    max_index = i

    li = get_left_child_i(i)
    if li <= len(data) - 1 and data[li] < data[max_index]:
        max_index = li

    ri = get_right_child_i(i)
    if ri <= len(data) - 1 and data[ri] < data[max_index]:
        max_index = ri

    if i != max_index:
        swaps.append((i, max_index))
        data[i], data[max_index] = data[max_index], data[i]
        sift_down(data, max_index, swaps)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)

    for i in range(n // 2 - 1, 0 - 1, -1):
        sift_down(data, i, swaps)

    return swaps


def test():
    a = [5, 4, 3, 2, 1]
    print(f'a: {a}')
    swaps = build_heap(a)
    print(f'a: {a} ; swaps: {swaps}')
    assert sorted(swaps) == sorted([(1, 4), (0, 1), (1, 3)])

    a = [1, 2, 3, 4, 5]
    print(f'a: {a}')
    swaps = build_heap(a)
    print(f'a: {a} ; swaps: {swaps}')
    assert sorted(swaps) == sorted([])

    print('OK')


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
    # test()
