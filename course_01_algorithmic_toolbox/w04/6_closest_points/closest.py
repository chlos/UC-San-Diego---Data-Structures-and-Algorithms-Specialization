#!/usr/bin/env python3

import sys
import math
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def test():
    x_arr = [7, 1, 4, 7]
    y_arr = [7, 100, 8, 7]
    res = minimum_distance(x_arr, y_arr)
    expected = 0.0
    print(f'result: {res} (expected: {expected})')
    assert res == expected

    x_arr = [0, 3]
    y_arr = [0, 4]
    res = minimum_distance(x_arr, y_arr)
    expected = 5.0
    print(f'result: {res} (expected: {expected})')
    assert res == expected

    print('OK')


def count_distance(p1, p2):
    return (
        math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    )


def minimum_distance_bruteforce(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            curr_dist = count_distance(points[i], points[j])
            if curr_dist < min_dist:
                min_dist = curr_dist

    return min_dist


def strip_min_dist(strip, curr_min_dist):
    min_dist = curr_min_dist
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j].y - strip[i].y) < min_dist:
            min_dist = count_distance(strip[i], strip[j])
            j += 1

    return min_dist


def minimum_distance_util(points_xsorted, points_ysorted):
    if len(points_xsorted) <= 3:
        return minimum_distance_bruteforce(points_xsorted)

    mid = len(points_xsorted) // 2
    # n = len(points_xsorted)     # FIXME
    # print(f'{points_xsorted}, len: {n}; mid: {mid}')  # FIXME
    mid_point = points_xsorted[mid]

    min_dist_l = minimum_distance_util(points_xsorted[:mid], points_ysorted)
    min_dist_r = minimum_distance_util(points_xsorted[mid:], points_ysorted)
    curr_min_dist = min(min_dist_l, min_dist_r)

    strip = []
    for point in points_xsorted:
        if abs(point.x - mid_point.x) < curr_min_dist:
            strip.append(point)

    return min(curr_min_dist, strip_min_dist(strip, curr_min_dist))


def minimum_distance(x, y):
    points = [Point(x_coord, y_coord) for x_coord, y_coord in zip(x, y)]
    # print(f'{points}')   # FIXME
    points_xsorted = sorted(points, key=lambda p: p.x)
    # print(f'sorted by x: {points_xsorted}')   # FIXME
    points_ysorted = sorted(points, key=lambda p: p.y)
    # print(f'sorted by y: {points_ysorted}')   # FIXME

    return minimum_distance_util(points_xsorted, points_ysorted)


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    _ = data[0]     # n
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))


if __name__ == '__main__':
    # test()
    main()