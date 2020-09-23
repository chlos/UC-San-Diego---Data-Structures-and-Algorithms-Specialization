# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def test():
    segments = [Segment(1, 3), Segment(2, 5), Segment(3, 6)]
    res = optimal_points(segments)
    print('===== {}'.format(res))
    assert res == [3]

    segments = [Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]
    res = optimal_points(segments)
    print('===== {}'.format(res))
    assert res == [3, 6]


def optimal_points(segments):
    segments.sort(key=lambda seg: seg.end)

    curr_point = -1
    points = []
    for s in segments:
        if s.start > curr_point:
            curr_point = s.end
            points.append(s.end)

    return points


def main():
    input = sys.stdin.read()
    _, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)


if __name__ == '__main__':
    # test()

    main()