# Uses python3
import sys


def test():
    a = [1, 5, 8, 12, 13]

    x = 8
    res = binary_search(a, x)
    print(f'res: {res}')
    assert res == 2
    x = 1
    res = binary_search(a, x)
    print(f'res: {res}')
    assert res == 0
    x = 23
    res = binary_search(a, x)
    print(f'res: {res}')
    assert res == -1

    print('OK')


def binary_search(a, x):
    left, right = 0, len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    _ = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        # replace with the call to binay_search when implemented
        print(binary_search(a, x), end=' ')


if __name__ == '__main__':
    # test()
    main()