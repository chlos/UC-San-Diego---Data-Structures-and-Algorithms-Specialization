# python3

# import sys
import os
# import threading
from collections import deque


def test():
    parents = [4, -1, 4, 1, 1]
    res = compute_height(len(parents), parents)
    exp = 3
    print(f'{parents}: {res} (exp: {exp})')
    assert res == exp

    for test_no in range(1, 24 + 1):
        test_file_path = os.path.join(os.path.dirname(__file__), 'tests', f'{test_no:02d}')
        with open(test_file_path) as test_file:
            _ = test_file.readline()
            test_data = list(map(int, test_file.readline().split()))
        test_data_part = test_data[0:11]
        test_data_len = len(test_data)
        ans_file_path = os.path.join(os.path.dirname(__file__), 'tests', f'{test_no:02d}.a')
        with open(ans_file_path) as ans_file:
            ans_data = int(ans_file.readline().strip())
        res = compute_height(test_data_len, test_data)
        print(f'#{test_no:02d} Test data: {test_data_part}... ({test_data_len} elements); expected ans: {ans_data}')
        print(f'Result: {res}')
        assert res == ans_data

    print('OK')


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return '{val}->({children})'.format(
            val=self.val,
            children=' '.join([str(child.val) for child in self.children])
        )


def get_height_recur(node):
    if node is None:
        return 0

    height = 0
    for child in node.children:
        height = max(height, get_height_recur(child))

    return height + 1


def get_height_iter(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    height = 0
    while queue:
        curr_queue_len = len(queue)
        for _ in range(curr_queue_len):
            node = queue.popleft()
            for child in node.children:
                queue.append(child)
        height += 1

    return height


def compute_height(n, parents):
    nodes = []
    for i in range(n):
        nodes.append(Node(i))
    # print(nodes)    # FIXME
    for child_i in range(n):
        parent_i = parents[child_i]
        if parent_i == -1:
            root_i = child_i
        else:
            nodes[parent_i].add_child(nodes[child_i])
    # print(nodes)    # FIXME

    # max_height = 0
    root = nodes[root_i]
    # max_height = get_height_recur(root)
    max_height = get_height_iter(root)

    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == "__main__":
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    # sys.setrecursionlimit(10**7)  # max depth of recursion
    # threading.stack_size(2**27)   # new thread will get stack of such size
    # threading.Thread(target=main).start()

    # test()
    main()