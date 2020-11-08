#!/usr/bin/env python3

def test():
    dataset = '5-8+7*4-8+9'
    res = get_maximum_value(dataset)
    exp = 200
    print(f'{dataset} max = {res} (expected: {exp})')
    assert res == exp

    print('OK')


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    digits = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    ops = [dataset[i] for i in range(1, len(dataset) - 1, 2)]

    dp_min = [[0] * len(digits) for _ in range(len(digits))]
    dp_max = [[0] * len(digits) for _ in range(len(digits))]
    for i in range(len(digits)):
        dp_min[i][i] = digits[i]
        dp_max[i][i] = digits[i]

    for s in range(len(digits)):
        for i in range(len(digits) - s - 1):
            j = i + s + 1
            min_val, max_val = get_min_max_val(i, j, ops, dp_min, dp_max)
            dp_min[i][j] = min_val
            dp_max[i][j] = max_val

    return dp_max[0][len(digits) - 1]


def get_min_max_val(i, j, ops, dp_min, dp_max):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = evalt(dp_max[i][k], dp_max[k + 1][j], ops[k])
        b = evalt(dp_max[i][k], dp_min[k + 1][j], ops[k])
        c = evalt(dp_min[i][k], dp_max[k + 1][j], ops[k])
        d = evalt(dp_min[i][k], dp_min[k + 1][j], ops[k])
        min_val = min(a, b, c, d, min_val)
        max_val = max(a, b, c, d, max_val)

    return min_val, max_val


def main():
    print(get_maximum_value(input()))


if __name__ == "__main__":
    # test()
    main()