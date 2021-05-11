#!/usr/bin/env python3
import sys


# e.g. {0:{'A':1,'T':2},1:{'C':3}}
def build_trie(patterns):
    tree = {0: {}}
    id_counter = 0

    for pattern in patterns:
        curr_node_id = 0
        for curr_char in pattern:

            # check if node already exists
            if curr_char in tree[curr_node_id]:
                curr_node_id = tree[curr_node_id][curr_char]
                continue

            # new node
            id_counter += 1
            new_node_id = id_counter
            tree[new_node_id] = {}
            tree[curr_node_id][curr_char] = new_node_id
            curr_node_id = new_node_id

    return tree


def solve(text, patterns):
    result = []
    trie = build_trie(patterns)

    for i_start in range(len(text)):
        i_curr = i_start
        curr_char = text[i_curr]
        curr_node_id = 0

        while True:
            # leaf
            if not trie[curr_node_id]:
                result.append(i_start)
                break
            # there is an edge with val == current char, let's move on
            elif curr_char in trie[curr_node_id]:
                curr_node_id = trie[curr_node_id][curr_char]
                i_curr += 1
                curr_char = text[i_curr] if i_curr < len(text) else None
            # no pattern for this subtext
            else:
                break

    return result


def test():
    pass


def main():
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for _ in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')


if __name__ == '__main__':
    test()
    main()