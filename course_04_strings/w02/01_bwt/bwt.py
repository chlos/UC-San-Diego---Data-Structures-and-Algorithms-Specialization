# python3
import sys
import collections


def BWT(text):
    bw_matrix = []
    text_deque = collections.deque(text)
    for _ in range(len(text)):
        bw_matrix.append(''.join(text_deque))
        ch = text_deque.popleft()
        text_deque.append(ch)

    bw_matrix.sort()

    bwt = ''
    for t in bw_matrix:
        bwt += t[-1]

    return bwt


def main():
    text = sys.stdin.readline().strip()
    print(BWT(text))


if __name__ == '__main__':
    # test()
    main()