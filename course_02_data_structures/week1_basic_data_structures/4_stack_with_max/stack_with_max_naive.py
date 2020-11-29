#!/usr/bin/env python3
import sys


def test():
    print('Test #1')
    stack = StackWithMax()
    stack.Push(2)
    stack.Push(1)
    assert stack.Max() == 2
    stack.Pop()
    assert stack.Max() == 2

    print('Test #2')
    stack = StackWithMax()
    stack.Push(1)
    stack.Push(2)
    assert stack.Max() == 2
    stack.Pop()
    assert stack.Max() == 1

    print('Test #3')
    stack = StackWithMax()
    stack.Push(2)
    stack.Push(3)
    stack.Push(9)
    stack.Push(7)
    stack.Push(2)
    assert stack.Max() == 9
    stack.Pop()
    assert stack.Max() == 9
    stack.Pop()
    assert stack.Max() == 9
    stack.Pop()
    assert stack.Max() == 3

    print('Test #4')
    stack = StackWithMax()
    stack.Push(1)
    stack.Push(2)
    stack.Push(2)
    assert stack.Max() == 2
    stack.Pop()
    assert stack.Max() == 2

    print('OK')


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

    def Max(self):
        assert(len(self.__stack))
        return self.__max[-1]


def main():
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)


if __name__ == '__main__':
    # test()
    main()