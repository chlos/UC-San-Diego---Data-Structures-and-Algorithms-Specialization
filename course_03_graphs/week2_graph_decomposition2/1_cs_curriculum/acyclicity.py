#!/usr/bin/env python3

import sys
from collections import defaultdict


def has_cycle_recur(adj, vertex, visited):
    if visited[vertex]:
        # has cycle!
        return True

    visited[vertex] = True
    for v in adj[vertex]:
        if has_cycle_recur(adj, v, visited):
            return True

    visited[vertex] = False
    return False


def acyclic(adj):
    visited = defaultdict(bool)
    for vertex, _ in enumerate(adj):
        if has_cycle_recur(adj, vertex, visited):
            return 1

    return 0


def has_cycle_recur_2(adj, vertex, visited):
    if visited[vertex] == -1:
        # has cycle!
        return True
    if visited[vertex] == 1:
        # processed, we can skip it
        return False

    visited[vertex] = -1
    for v in adj[vertex]:
        if has_cycle_recur(adj, v, visited):
            return True

    visited[vertex] = 1
    return False


def acyclic_2(adj):
    # 0: not visited
    # 1: processed, OK
    # -1: is being processed, visited again, CYCLE
    visited = [0] * len(adj)
    for vertex in range(len(adj)):
        if has_cycle_recur(adj, vertex, visited):
            return 1

    return 0


def test(f):
    adj = [[1], [2], [0], [0]]
    res = f(adj)
    exp = 1
    print(f'res: {res} (exp {exp})\n')
    assert res == exp

    adj = [[1, 2, 3], [2, 4], [3, 4], [], []]
    res = f(adj)
    exp = 0
    print(f'res: {res} (exp {exp})\n')
    assert res == exp

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
    # print(adj)   # FIXME
    print(acyclic(adj))


if __name__ == '__main__':
    # test(acyclic)
    # test(acyclic_2)
    main()