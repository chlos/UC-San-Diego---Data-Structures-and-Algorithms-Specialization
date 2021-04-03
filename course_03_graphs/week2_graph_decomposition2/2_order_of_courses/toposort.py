# Uses python3

import sys


def dfs(adj, used, order, x):
    used[x] = 1
    for v in adj[x]:
        if not used[v]:
            dfs(adj, used, order, v)

    order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for vertex in range(len(adj)):
        if not used[vertex]:
            dfs(adj, used, order, vertex)

    order.reverse()
    return order


def toposort_iter_stack(adj):
    # count incoming edges per vertex
    in_edges_per_vertex = [0] * len(adj)
    for vertex in range(len(adj)):
        for vertex_dst in adj[vertex]:
            in_edges_per_vertex[vertex_dst] += 1

    # vertices with no incoming edges
    queue = []
    for vertex in range(len(adj)):
        if in_edges_per_vertex[vertex] == 0:
            queue.append(vertex)

    order = []
    count_visited = 0
    while queue:
        vertex = queue.pop(0)
        order.append(vertex)
        count_visited += 1

        # 'remove' edges from popped vertex
        for vertex_dst in adj[vertex]:
            in_edges_per_vertex[vertex_dst] -= 1
            if in_edges_per_vertex[vertex_dst] == 0:
                queue.append(vertex_dst)

    if count_visited == len(adj):
        return order
    else:
        # there was a cycle somewhere in the graph
        return None


def test():
    adj = [[1], [], [0], [0]]
    exp = [[3, 2, 0, 1], [2, 3, 0, 1]]
    result = toposort(adj)
    print(f'result: {result} (expected: {exp})')
    assert result in exp

    adj = [[], [], [0], []]
    exp = [[1, 2, 3, 0], [3, 2, 1, 0]]
    result = toposort(adj)
    print(f'result: {result} (expected: {exp})')
    assert result in exp

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
    # print(adj)  # FIXME
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')


if __name__ == '__main__':
    # test()
    main()