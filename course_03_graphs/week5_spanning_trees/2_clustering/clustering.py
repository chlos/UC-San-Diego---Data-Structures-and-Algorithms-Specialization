#!/usr/bin/env python3

import sys
import math


def clustering(x, y, k):
    # FIXME
    return -1.


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))


if __name__ == '__main__':
    pass