#!/usr/bin/env python3

import sys

sys.setrecursionlimit(200000)


def get_stack(adj, visited, stack, x):
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            get_stack(adj, visited, stack, vertex)
    stack.append(x)


def dfs(adj, visited, x):
    # print(x)
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            dfs(adj, visited, vertex)


def get_inverted_graph(adj):
    inverted = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            inverted[j].append(i)
    return inverted


def number_of_strongly_connected_components(adj):
    result = 0

    visited = [False] * len(adj)
    stack = []
    for vertex in range(len(adj)):
        if not visited[vertex]:
            get_stack(adj, visited, stack, vertex)
    # print(f'stack: {stack}')

    adj_inverted = get_inverted_graph(adj)
    # print(f'adj_inverted: {adj_inverted}')

    visited = [False] * len(adj)
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            # print(f'dfs vertex {vertex}')
            dfs(adj_inverted, visited, vertex)
            result += 1

    return result


def test():
    adj = [[1], [2], [0], [0]]
    exp = 2
    result = number_of_strongly_connected_components(adj)
    print(f'result: {result} (expected: {exp})')
    assert result == exp

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
    # print(f'adj: {adj}')    # FIXME
    print(number_of_strongly_connected_components(adj))


if __name__ == '__main__':
    # test()
    main()