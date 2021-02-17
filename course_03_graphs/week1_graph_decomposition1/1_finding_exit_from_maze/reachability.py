#!/usr/bin/env python3

import sys
from collections import defaultdict


# iter DFS
def reach(adj, x, y):
    visited = defaultdict(bool)
    stack = [x]
    while stack:
        vertex = stack.pop()
        visited[vertex] = True
        if vertex == y:
            return 1

        for v in adj[vertex]:
            if not visited[v]:
                stack.append(v)

    return 0


def reach_recur(adj, x, y):
    def dfs(adj, vertex, dst_vertex, visited):
        if vertex == dst_vertex:
            return True

        visited[vertex] = True

        for v in adj[vertex]:
            if not visited[v]:
                if dfs(adj, v, dst_vertex, visited):
                    return True
        return False

    visited = defaultdict(bool)
    if dfs(adj, x, y, visited):
        return 1
    return 0


def test():
    adj = [
        [1, 3],
        [0, 2],
        [1, 3],
        [2, 0]
    ]
    x, y = 0, 3
    result = reach(adj, x, y)
    expected = 1
    print(f'res: {result} (exp: {expected})')
    assert result == expected

    adj = [
        [1],
        [0, 2],
        [1],
        []
    ]
    x, y = 0, 3
    result = reach(adj, x, y)
    expected = 0
    print(f'res: {result} (exp: {expected})')
    assert result == expected

    adj = [
        [20, 89], [90], [], [], [82, 65], [8, 71, 30], [18, 90, 92, 35], [49], [5], [67, 88, 38], [88, 71, 60, 79],
        [21, 85], [71, 76, 66], [], [22, 16], [49], [82, 81, 14], [87], [6, 75, 66], [97, 53, 39, 90], [93, 0, 54, 49],
        [67, 57, 11, 68], [52, 55, 14], [75, 68], [60], [63, 56], [95], [41, 58, 73, 51], [], [31, 95, 52], [34, 5],
        [92, 29, 45], [], [93, 95], [30], [6], [37, 90], [85, 36, 43], [72, 9], [70, 19, 90], [], [97, 27, 94], [51],
        [74, 37, 93, 78, 53], [90], [31], [], [], [], [7, 15, 68, 65, 20], [], [42, 27], [22, 83, 29], [19, 43],
        [88, 72, 20], [22, 78], [25], [21], [27], [], [10, 24], [70], [91, 71], [25], [], [88, 49, 98, 4],
        [89, 67, 18, 12], [21, 66, 9], [49, 21, 73, 23], [], [74, 83, 39, 87, 61], [5, 62, 10, 12, 78], [54, 38],
        [27, 68], [70, 43], [99, 18, 23, 92], [12], [], [55, 71, 43], [10], [97], [16], [16, 4], [70, 52], [],
        [37, 11], [], [17, 70], [10, 54, 65, 9], [66, 0], [44, 36, 6, 1, 39, 19], [62, 94], [31, 75, 6], [20, 43, 33],
        [41, 91], [26, 29, 33], [], [80, 41, 19], [65], [75]
    ]
    # for vertex, lst in enumerate(adj):
    #     print(vertex, lst)
    x, y = 41, 45
    result = reach(adj, x, y)
    expected = 1
    print(f'res: {result} (exp: {expected})')
    assert result == expected

    print('OK')


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    # print(edges)  # FIXME
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # print(adj)  # FIXME
    print(reach(adj, x, y))


if __name__ == '__main__':
    # test()
    main()