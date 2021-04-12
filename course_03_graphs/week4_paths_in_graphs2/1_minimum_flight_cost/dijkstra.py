#!/usr/bin/env python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    # queue elements: (DIST, VERTEX)
    prio_queue = queue.PriorityQueue()

    dist[s] = 0
    prio_queue.put((dist[s], s))
    while not prio_queue.empty():
        _, curr_v = prio_queue.get()

        for cost_idx, curr_v_neighbour in enumerate(adj[curr_v]):
            if dist[curr_v_neighbour] > dist[curr_v] + cost[curr_v][cost_idx]:
                dist[curr_v_neighbour] = dist[curr_v] + cost[curr_v][cost_idx]
                prio_queue.put((dist[curr_v_neighbour], curr_v_neighbour))

    if dist[t] == float('inf'):
        return -1
    return dist[t]


def test():
    adj = [[1, 2], [2], [], [0]]
    cost = [[1, 5], [2], [], [2]]
    s, t = 0, 2
    res = distance(adj, cost, s, t)
    exp = 3
    print(f'res: {res} (exp {exp})')
    assert res == exp

    print('OK')


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
    s, t = data[0] - 1, data[1] - 1
    # print(f'adj: {adj} ; cost: {cost} ; s, t = {s}, {t}')   # FIXME
    print(distance(adj, cost, s, t))


if __name__ == '__main__':
    test()
    main()