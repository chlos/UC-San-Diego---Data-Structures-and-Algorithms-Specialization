#!/usr/bin/env python3

import sys
import queue


def get_inverted_colour(curr_colour):
    if curr_colour == 1:
        return 2
    if curr_colour == 2:
        return 1


def bfs(adj, colours, vertex):
    q = queue.Queue()

    q.put(vertex)
    colours[vertex] = 1

    while not q.empty():
        vertex = q.get()
        for adj_vertex in adj[vertex]:
            if colours[adj_vertex] == colours[vertex]:
                return 0
            elif colours[adj_vertex] is None:
                colours[adj_vertex] = get_inverted_colour(colours[vertex])
                q.put(adj_vertex)

    return 1


def bipartite(adj):
    colours = [None] * len(adj)
    for v in range(len(adj)):
        if colours[v] is not None:
            continue
        if not bfs(adj, colours, v):
            return 0

    return 1


def test():
    adj = [[1, 3, 2], [0, 2], [1, 0], [0]]
    is_bipartite = bipartite(adj)
    expected = 0
    print(f'result: {is_bipartite} (expected: {expected})')
    assert is_bipartite == expected

    adj = [[3], [4, 3], [3], [1, 2, 0], [1]]
    is_bipartite = bipartite(adj)
    expected = 1
    print(f'result: {is_bipartite} (expected: {expected})')
    assert is_bipartite == expected

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
    # print(adj)  # FIXME
    print(bipartite(adj))


if __name__ == '__main__':
    # test()
    main()