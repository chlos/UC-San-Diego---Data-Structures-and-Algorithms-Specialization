#!/usr/bin/env python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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


def test():
    patterns = ['ATA']
    trie = build_trie(patterns)
    exp = {0: {'A': 1}, 1: {'T': 2}, 2: {'A': 3}, 3: {}}
    print(f'{trie}\n{exp} - expected')
    assert trie == exp

    patterns = ['AT', 'AG', 'AC']
    trie = build_trie(patterns)
    exp = {0: {'A': 1}, 1: {'T': 2, 'G': 3, 'C': 4}, 2: {}, 3: {}, 4: {}}
    print(f'{trie}\n{exp} - expected')
    assert trie == exp

    print('OK')


def main():
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))


if __name__ == '__main__':
    # test()
    main()