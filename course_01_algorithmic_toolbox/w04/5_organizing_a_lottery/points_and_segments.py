# Uses python3
import sys
from collections import namedtuple
from bisect import (
    bisect_left,
    bisect_right,
)


def test(f):
    starts = [0, 7]
    ends = [5, 10]
    points = [1, 6, 11]
    res = f(starts, ends, points)
    expected = [1, 0, 0]
    print(f'result: {res} (expected: {expected})')
    assert res == expected
    print('OK')


def binsearch_count_segments(starts, ends, points):
    starts = sorted(starts)
    ends = sorted(ends)

    counts = [len(starts)] * len(points)
    for i, point in enumerate(points):
        counts[i] -= bisect_left(ends, point)
        counts[i] -= len(starts) - bisect_right(starts, point)

    return counts


def fast_count_segments(starts, ends, points):
    events = []
    Event = namedtuple('Event', ['coord', 'type', 'index'])
    for coord in starts:
        events.append(Event(coord, 'l', None))
    for i, coord in enumerate(points):
        events.append(Event(coord, 'p', i))
    for coord in ends:
        events.append(Event(coord, 'r', None))
    events = sorted(events)

    cnt = [0] * len(points)
    curr_segments = 0
    for event in events:
        if event.type == 'l':
            curr_segments += 1
        elif event.type == 'p':
            cnt[event.index] = curr_segments
        elif event.type == 'r':
            curr_segments -= 1

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    _ = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # cnt = naive_count_segments(starts, ends, points)
    # cnt = fast_count_segments(starts, ends, points)
    cnt = binsearch_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')


if __name__ == '__main__':
    # test(fast_count_segments)
    # test(binsearch_count_segments)
    main()