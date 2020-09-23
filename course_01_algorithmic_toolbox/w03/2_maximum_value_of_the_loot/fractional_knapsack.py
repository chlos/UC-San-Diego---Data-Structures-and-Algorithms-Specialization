# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    # sort items by cost per weight
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    i = 0
    value = 0.
    capacity_left = capacity
    while capacity_left > 0 and i < len(items):
        item_value, item_weight = items[i]
        if capacity_left >= item_weight:
            value += item_value
            capacity_left -= item_weight
        else:
            ratio = item_weight / capacity_left
            value += item_value / ratio
            capacity_left -= item_weight / ratio
        i += 1

    return value


def test():
    capacity = 50
    values = [60, 100, 120]
    weights = [20, 50, 30]
    result = get_optimal_value(capacity, weights, values)
    print('===== {}'.format(result))
    assert result == 180.0

    capacity = 10
    values = [500]
    weights = [30]
    result = get_optimal_value(capacity, weights, values)
    print('===== {}'.format(result))
    assert result == 500 / 3

    print('OK')


if __name__ == "__main__":
    # test()  # FIXME

    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))