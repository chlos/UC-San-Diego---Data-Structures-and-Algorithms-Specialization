import sys


def test():
    a = [21, 2]
    res = largest_number(a)
    print('===== {}'.format(res))
    assert int(res) == 221


def is_greater_or_equal(num1, num2):
    return int(str(num1) + str(num2)) >= int(str(num2) + str(num1))


def largest_number(a):
    res = ""
    while a:
        max_num = 0
        for curr_num in a:
            if is_greater_or_equal(curr_num, max_num):
                max_num = curr_num
        res += str(max_num)
        a.remove(max_num)

    return res


def main():
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))


if __name__ == '__main__':
    # test()
    main()