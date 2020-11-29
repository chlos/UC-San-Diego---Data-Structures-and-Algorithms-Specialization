# python3

from collections import deque
# import heapq


def test():
    print('Test QueueWithMax')
    q = QueueWithMax()
    q.Push(1)
    assert q.Max() == 1
    assert q.Pop() == 1
    q.Push(1)
    q.Push(2)
    assert q.Max() == 2
    assert q.Pop() == 1
    assert q.Pop() == 2
    q.Push(1)
    q.Push(1)
    assert q.Max() == 1
    assert q.Pop() == 1
    assert q.Pop() == 1
    q.Push(1)
    q.Push(2)
    q.Push(5)
    q.Push(3)
    q.Push(4)
    assert q.Max() == 5
    assert q.Pop() == 1
    assert q.Max() == 5
    assert q.Pop() == 2
    assert q.Max() == 5
    assert q.Pop() == 5
    assert q.Max() == 4
    print('QueueWithMax: OK')

    print('Test max_sliding_window()')
    sequence = [2, 7, 3, 1, 5, 2, 6, 2]
    m = 4
    assert max_sliding_window(sequence, m) == [7, 7, 5, 6, 6]
    print('max_sliding_window(): OK')


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.__max or a >= self.__max[-1]:
            self.__max.append(a)

    def Pop(self):
        assert(len(self.__stack))
        pop_val = self.__stack.pop()
        if self.__max and self.__max[-1] == pop_val:
            self.__max.pop()

        return pop_val

    def Max(self):
        assert(len(self.__stack))
        return self.__max[-1]

    def Empty(self):
        if self.__stack:
            return False
        else:
            return True


class QueueWithMax():
    def __init__(self):
        self.__stack_in = StackWithMax()
        self.__stack_out = StackWithMax()

    def Push(self, val):
        self.__stack_in.Push(val)

    def Pop(self):
        if self.__stack_out.Empty():
            while not self.__stack_in.Empty():
                self.__stack_out.Push(self.__stack_in.Pop())
        return self.__stack_out.Pop()

    def Max(self):
        if self.__stack_out.Empty():
            return self.__stack_in.Max()
        elif self.__stack_in.Empty():
            return self.__stack_out.Max()
        else:
            return max(self.__stack_out.Max(), self.__stack_in.Max())


def max_sliding_window_queue_with_max(sequence, m):
    maximums = []
    q = QueueWithMax()

    for i in range(m):
        q.Push(sequence[i])
    maximums.append(q.Max())

    for i in range(m, len(sequence)):
        q.Pop()
        q.Push(sequence[i])
        maximums.append(q.Max())

    return maximums


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


# https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation
def max_sliding_window(sequence, m):
    maximums = []
    # deque with num indeces
    q = deque()

    for i in range(len(sequence)):
        # check q size vs window size
        if q and q[0] < i - m + 1:
            q.popleft()

        # pop elements which will not be maximums in current window
        while q and sequence[q[-1]] < sequence[i]:
            q.pop()

        q.append(i)

        if i >= m - 1:
            maximums.append(sequence[q[0]])

    return maximums


def main():
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))


if __name__ == '__main__':
    # test()
    main()