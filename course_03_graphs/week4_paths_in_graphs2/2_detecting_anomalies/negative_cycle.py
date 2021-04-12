#!/usr/bin/env python3

import sys


def negative_cycle(adj, cost):
    distance = [sys.maxsize] * len(adj)
    parents = [None] * len(adj)

    distance[0] = 0
    # outer loop that runs V-1 times
    for _ in range(len(adj) - 1):
        # inner loop to run for all the vertex in graph
        for vertex in range(len(adj)):
            # check for all the edges of current vertex
            for cost_index, neighbour in enumerate(adj[vertex]):
                neighbour_cost = cost[vertex][cost_index]
                # Relax the edges i.e update the cost if its less than the previous stored cost
                if distance[neighbour] > distance[vertex] + neighbour_cost:
                    distance[neighbour] = distance[vertex] + neighbour_cost
                    parents[neighbour] = vertex

    # Relax all edges again and if we get any edge decreasing it means there exists a negative cycle
    for vertex in range(len(adj)):
        for cost_index, neighbour in enumerate(adj[vertex]):
            neighbour_cost = cost[vertex][cost_index]
            if distance[neighbour] > distance[vertex] + neighbour_cost:
                return 1
    return 0


def test():
    pass


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))


if __name__ == '__main__':
    test()
    main()