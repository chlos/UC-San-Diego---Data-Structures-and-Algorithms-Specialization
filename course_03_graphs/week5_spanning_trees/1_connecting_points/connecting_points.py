#!/usr/bin/env python3

import math
import heapq


def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def minimum_distance(points):
    costs = [float('inf')] * len(points)
    costs[0] = 0

    min_queue = []
    for i in range(len(points)):
        # (dist, index)
        min_queue.append((float('inf'), i))
    min_queue[0] = (0, 0)

    while min_queue:
        _, curr_point_i = heapq.heappop(min_queue)

        for i in range(len(min_queue)):
            neighbour_point_dist, neighbout_point_i = min_queue[i]
            dist = get_distance(points[curr_point_i], points[neighbout_point_i])
            if neighbour_point_dist > dist:
                min_queue[i] = (dist, neighbout_point_i)
                costs[neighbout_point_i] = dist

        heapq.heapify(min_queue)

    return sum(costs)


if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print("{0:.9f}".format(minimum_distance(points)))