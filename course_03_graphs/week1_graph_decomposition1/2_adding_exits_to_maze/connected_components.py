#!/usr/bin/env python3

import sys
from collections import defaultdict


def dfs(adj, vertex, connections_count, visited):
    visited[vertex] = True

    for v in adj[vertex]:
        if not visited[v]:
            dfs(adj, v, connections_count, visited)


def number_of_components(adj):
    visited = defaultdict(bool)
    connections_count = 0

    for vertex, _ in enumerate(adj):
        if not visited[vertex]:
            dfs(adj, vertex, connections_count, visited)
            connections_count += 1

    return connections_count


def test():
    adj = [
        [1], [0, 2], [1], []
    ]
    result = number_of_components(adj)
    expected = 2
    print(f'res: {result} (exp: {expected})')
    assert result == expected

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
    print(number_of_components(adj))


if __name__ == '__main__':
    # test()
    main()