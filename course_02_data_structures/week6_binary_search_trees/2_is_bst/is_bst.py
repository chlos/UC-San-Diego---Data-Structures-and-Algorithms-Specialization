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
        if node_key <= lower or node_key >= upper:
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


def inOrder(tree):
    result = []
    if not tree:
        return result

    stack = []
    node = 0
    while stack or node != -1:
        if node != -1:
            stack.append(node)
            left_node = tree[node][1]
            node = left_node
        else:
            tmp_node = stack.pop()
            result.append(tree[tmp_node][0])
            right_node = tree[tmp_node][2]
            node = right_node

    return result


def IsBinarySearchTree_iter_1(tree):
    if not tree:
        return True

    sorted_tree = inOrder(tree)
    # print(f'sorted: {sorted_tree}')
    is_sorted = all(sorted_tree[i] <= sorted_tree[i + 1] for i in range(len(sorted_tree) - 1))
    return is_sorted


def IsBinarySearchTree_iter_2(tree):
    if not tree:
        return True

    stack = []
    prev_node = -1
    node = 0
    while node != -1 or stack:
        while node != -1:
            stack.append(node)
            left_node = tree[node][1]
            node = left_node

        node = stack.pop()
        if prev_node != -1 and tree[prev_node][0] >= tree[node][0]:
            return False
        prev_node = node
        right_node = tree[node][2]
        node = right_node

    return True


def test():
    data = [
        [4, 1, 2],
        [2, 3, 4],
        [5, -1, -1],
        [1, -1, -1],
        [3, -1, -1],
    ]
    assert IsBinarySearchTree(data) is True

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
         4
        /
       2
      / \
    1    5
    '''
    print()
    data = [
        [4, 1, -1],
        [2, 2, 3],
        [1, -1, -1],
        [5, -1, -1],
    ]
    assert IsBinarySearchTree(data) is False

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