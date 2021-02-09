# python3

import sys
import threading
# max depth of recursion
sys.setrecursionlimit(10**6)
# new thread will get stack of such size
threading.stack_size(2**27)


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def read_debug(self, data):
        self.n = len(data)
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i, (a, b, c) in enumerate(data):
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

        print(f'keys: {self.key}\nleft: {self.left}\nrght: {self.right}')

    def inOrder_recur(self):
        def traverse(node_i):
            if node_i == -1:
                return
            traverse(self.left[node_i])
            self.result.append(self.key[node_i])
            traverse(self.right[node_i])

        self.result = []
        traverse(0)

        return self.result

    def inOrder(self):
        self.result = []

        stack = []
        node = 0
        while stack or node != -1:
            if node != -1:
                stack.append(node)
                node = self.left[node]
            else:
                tmp_node = stack.pop()
                self.result.append(self.key[tmp_node])
                node = self.right[tmp_node]

        return self.result

    def preOrder_recur(self):
        def traverse(node_i):
            if node_i == -1:
                return
            self.result.append(self.key[node_i])
            traverse(self.left[node_i])
            traverse(self.right[node_i])

        self.result = []
        traverse(0)

        return self.result

    def preOrder(self):
        self.result = []

        stack = [0]
        while stack:
            node = stack.pop()
            if node == -1:
                continue
            self.result.append(self.key[node])
            stack.append(self.right[node])
            stack.append(self.left[node])

        return self.result

    def postOrder_recur(self):
        def traverse(node_i):
            if node_i == -1:
                return
            traverse(self.left[node_i])
            traverse(self.right[node_i])
            self.result.append(self.key[node_i])

        self.result = []
        traverse(0)

        return self.result

    def postOrder(self):
        self.result = []

        stack = [(0, False)]
        while stack:
            node, visited = stack.pop()
            if node == -1:
                continue
            if visited:
                self.result.append(self.key[node])
            else:
                stack.append((node, True))
                stack.append((self.right[node], False))
                stack.append((self.left[node], False))

        return self.result


def test():
    data = [
        [4, 1, 2],
        [2, 3, 4],
        [5, -1, -1],
        [1, -1, -1],
        [3, -1, -1],
    ]
    tree = TreeOrders()
    tree.read_debug(data)
    inorder = tree.inOrder()
    preorder = tree.preOrder()
    postorder = tree.postOrder()
    print(f'inorder: {inorder}\npre: {preorder}\npost: {postorder}')


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == "__main__":
    # test()
    main()


threading.Thread(target=main).start()