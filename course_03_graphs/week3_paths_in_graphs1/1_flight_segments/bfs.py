#!/usr/bin/env python3

import sys
import queue


def distance(adj, s, t):
    dist = [float('inf')] * len(adj)

    q = queue.Queue()
    q.put(s)
    dist[s] = 0

    while not q.empty():
        vertex = q.get()
        if vertex == t:
            return dist[vertex]

        for dst_vertex in adj[vertex]:
            if dist[dst_vertex] == float('inf'):
                dist[dst_vertex] = dist[vertex] + 1
                q.put(dst_vertex)

    return -1


def test():
    adj = [[1, 3, 2], [0, 2], [1, 0], [0]]
    s, t = 1, 3
    dist_expected = 2
    dist_actual = distance(adj, s, t)
    print(f'dist: {dist_actual} (expected: {dist_expected})')
    assert dist_actual == dist_expected

    adj = [[2, 3], [4], [0, 3], [2, 0], [1]]
    s, t = 2, 4
    dist_expected = -1
    dist_actual = distance(adj, s, t)
    print(f'dist: {dist_actual} (expected: {dist_expected})')
    assert dist_actual == dist_expected

    adj = [[1], [0, 2], [1, 3], [2]]
    s, t = 0, 2
    dist_expected = 2
    dist_actual = distance(adj, s, t)
    print(f'dist: {dist_actual} (expected: {dist_expected})')
    assert dist_actual == dist_expected

    print('OK')


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    # print(f'===== adj: {adj}, s, t: {s}, {t}')  # FIXME
    print(distance(adj, s, t))


if __name__ == '__main__':
    # test()
    main()