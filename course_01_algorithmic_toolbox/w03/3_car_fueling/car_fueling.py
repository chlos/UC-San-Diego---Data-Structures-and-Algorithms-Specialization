# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    refuels = 0
    i = 0
    last_refuel = 0
    while i < len(stops):
        if stops[i] - last_refuel > tank:
            if stops[i] - stops[i - 1] > tank:
                return -1
            last_refuel = stops[i - 1]
            refuels += 1
        i += 1

    return refuels


def test():
    d = 950     # destination
    m = 400     # miles on one tank
    stops = [200, 375, 550, 750]
    res = compute_min_refills(d, m, stops)
    print('===== {}'.format(res))
    assert res == 2

    d = 10     # destination
    m = 3     # miles on one tank
    stops = [1, 2, 5, 9]
    res = compute_min_refills(d, m, stops)
    print('===== {}'.format(res))
    assert res == -1


if __name__ == '__main__':
    # test()

    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
