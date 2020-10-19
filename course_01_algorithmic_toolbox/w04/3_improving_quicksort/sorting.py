# Uses python3
import sys
import random


def test():
    a = [6, 4, 1, 7, 2, 10]
    expected = sorted(a)
    randomized_quick_sort(a, 0, len(a) - 1)
    print(f'exp: {expected}\nres: {a}\n')
    assert a == expected

    print('OK')


def partition3_tmp(a, l, r):
    print(f'before: {a} ({l}...{r})')
    x = a[l]
    # j: last 'less than' element
    j = l
    # e: last 'equal' element
    e = l
    # i: last 'greater than' element
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            j += 1
            a[i], a[j] = a[j], a[i]
            e += 1
            a[j], a[e] = a[e], a[j]

    # a[l], a[j] = a[j], a[l]
    print(f'after: {a} (e: {e} j: {j})    x: {x}')
    return e, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def partition3(a, l, r):
    pivot = a[l]
    # 1st 'equal' element; lt_end+1 is the last elem of 'less than' interval
    lt_end = l
    # last 'equal' element; gt_begin+1 is the first elem of 'greater than' interval
    gt_begin = r

    i = l
    while i <= gt_begin:
        if a[i] < pivot:
            a[lt_end], a[i] = a[i], a[lt_end]
            i += 1
            lt_end += 1
        elif a[i] > pivot:
            a[i], a[gt_begin] = a[gt_begin], a[i]
            gt_begin -= 1
        elif a[i] == pivot:
            i += 1

    return lt_end, gt_begin


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    lt_end, gt_begin = partition3(a, l, r)
    randomized_quick_sort(a, l, lt_end - 1)
    randomized_quick_sort(a, gt_begin + 1, r)


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


if __name__ == '__main__':
    # test()
    main()