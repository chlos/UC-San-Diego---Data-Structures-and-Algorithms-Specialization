#!/usr/bin/python3

import sys
import threading

# max depth of recursion
sys.setrecursionlimit(2 * 10**9)
# new thread will get stack of such size
threading.stack_size(2**32)


def IsBinarySearchTree(tree):
    def is_bin_recur(node, lower=float('-inf'), upper=float('inf')):
        if node == -1:
            return True

        node_key = tree[node][0]
        if node_key < lower or node_key >= upper:
            return False

        left_node = tree[node][1]
        if not is_bin_recur(left_node, lower, node_key):
            return False
        right_node = tree[node][2]
        if not is_bin_recur(right_node, node_key, upper):
            return False

        return True

    if not tree:
        return True
    return is_bin_recur(0)


# iter
def IsBinarySearchTree_iter(tree):
    if not tree:
        return True

    stack = []
    prev_node = (-1, None)
    node = (0, False)
    node_i, _ = node
    while node_i != -1 or stack:
        while node_i != -1:
            stack.append(node)
            left_node_i = tree[node_i][1]
            node = (left_node_i, False)
            node_i, _ = node

        node = stack.pop()
        node_i, is_right = node
        prev_node_i, _ = prev_node
        if prev_node_i != -1 and (
            not is_right and tree[prev_node_i][0] >= tree[node_i][0] or
            is_right and tree[prev_node_i][0] > tree[node_i][0]
        ):
            return False
        prev_node = node
        right_node_i = tree[node_i][2]
        node = (right_node_i, True)
        node_i, _ = node

    return True


def test():
    '''
       1
      /\
     2  3
    '''
    print()
    data = [
        [1, 1, 2],
        [2, -1, -1],
        [3, -1, -1],
    ]
    assert IsBinarySearchTree(data) is False

    '''
       2
      /\
     2  3
    '''
    print()
    data = [
        [2, 1, 2],
        [2, -1, -1],
        [3, -1, -1],
    ]
    assert IsBinarySearchTree(data) is False

    '''
       2
      /\
     1  2
    '''
    print()
    data = [
        [2, 1, 2],
        [1, -1, -1],
        [2, -1, -1],
    ]
    assert IsBinarySearchTree(data) is True

    print('OK')


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for _ in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    # test()
    # main()
    threading.Thread(target=main).start()