# Uses python3
import sys


def test():
    a = [2, 3, 9, 2, 9]
    b = len(a) * [0]
    res = get_number_of_inversions(a, b, 0, len(a) - 1)
    print(a, res)
    assert res == 2

    a = [1, 2, 3, 4, 5, 6]
    b = len(a) * [0]
    res = get_number_of_inversions(a, b, 0, len(a) - 1)
    print(a, res)
    assert res == 0

    a = [9, 8, 7, 3, 2, 1]
    b = len(a) * [0]
    res = get_number_of_inversions(a, b, 0, len(a) - 1)
    print(a, res)
    assert res == 15

    print('OK')


def merge(arr, arr_tmp, left, mid, right):
    number_of_inversions = 0
    # start of 1st sub-array
    i = left
    # start of 2nd sub-array
    j = mid + 1
    # start of tmp merged array
    k_tmp = left
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            arr_tmp[k_tmp] = arr[i]
            i += 1
        else:
            arr_tmp[k_tmp] = arr[j]
            j += 1
            number_of_inversions += (mid - i + 1)
        k_tmp += 1

    # copy the remaining elements of sub-arrays
    while i <= mid:
        arr_tmp[k_tmp] = arr[i]
        i += 1
        k_tmp += 1
    while j <= right:
        arr_tmp[k_tmp] = arr[j]
        j += 1
        k_tmp += 1
    # tmp -> arr
    for i in range(left, right + 1):
        arr[i] = arr_tmp[i]

    return number_of_inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left < 1:
        return number_of_inversions

    mid = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, mid)
    number_of_inversions += get_number_of_inversions(a, b, mid + 1, right)

    number_of_inversions += merge(a, b, left, mid, right)

    return number_of_inversions


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))


if __name__ == '__main__':
    # test()
    main()