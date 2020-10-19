# Uses python3
import sys


def test(f):
    a = [2, 3, 9, 2, 2]
    res = f(a, 0, len(a))
    print(f'=== {a}: {res}')
    assert res != -1

    a = [1, 2, 3, 4]
    res = f(a, 0, len(a))
    print(f'=== {a}: {res}')
    assert res == -1

    a = [1, 2, 3, 1]
    res = f(a, 0, len(a))
    print(f'=== {a}: {res}')
    assert res == -1

    print('OK')


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = left + (right - left) // 2
    left_maj = get_majority_element(a, left, mid)
    right_maj = get_majority_element(a, mid, right)

    left_maj_count = 0
    if left_maj != -1:
        left_maj_count = sum(1 for i in range(left, right) if a[i] == left_maj)
    right_maj_count = 0
    if right_maj != -1:
        right_maj_count = sum(1 for i in range(left, right) if a[i] == right_maj)

    if left_maj_count > (right - left) // 2:
        return left_maj
    if right_maj_count > (right - left) // 2:
        return right_maj

    return -1


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    # test(get_majority_element)

    main()