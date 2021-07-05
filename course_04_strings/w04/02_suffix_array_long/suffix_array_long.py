# python3
import sys


CHAR_N = 256


def sort_characters(text_str):
    ts_len = len(text_str)
    counts = [0 for i in range(CHAR_N)]
    order = [None for i in range(ts_len)]

    # get the total number of individual items
    for char in text_str:
        counts[ord(char)] += 1

    # recompute starting positions in array to be returned (order)
    for j, _ in enumerate(counts):
        counts[j] = counts[j] + counts[j - 1]

    # load reversed characters (as ints) into order array
    for i in range(ts_len - 1, -1, -1):
        c = ord(text_str[i])
        counts[c] = counts[c] - 1
        order[counts[c]] = i
    return order


def compute_char_classes(str_text, order_arr):
    s_len = len(str_text)
    res_class = [None for i in range(s_len)]
    res_class[order_arr[0]] = 0
    for i in range(1, s_len):
        if str_text[order_arr[i]] != str_text[order_arr[i - 1]]:
            res_class[order_arr[i]] = res_class[order_arr[i - 1]] + 1
        else:
            res_class[order_arr[i]] = res_class[order_arr[i - 1]]
    return res_class


def sort_doubled(str_text, length, order, res_cls):
    len_text = len(str_text)
    count = [0 for i in range(len_text)]
    new_order = [None for i in range(len_text)]
    for i in range(len_text):
        count[res_cls[i]] += 1
    for j in range(1, len_text):
        count[j] += count[j - 1]
    for ind in range(len_text - 1, -1, -1):
        start = (order[ind] - length + len_text) % len_text
        cl = res_cls[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, cls, length):
    len_no = len(new_order)
    new_cls = [0 for i in range(len_no)]
    new_cls[new_order[0]] = 0

    for i in range(1, len_no):
        cur = new_order[i]
        prev = new_order[i - 1]
        mid = (cur + length)
        mid_prev = (prev + length) % len_no
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            new_cls[cur] = new_cls[prev] + 1
        else:
            new_cls[cur] = new_cls[prev]
    return new_cls


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sort_characters(text)
    txt_len = len(text)
    cls = compute_char_classes(text, order)
    length = 1
    while length < txt_len:
        order = sort_doubled(text, length, order, cls)
        cls = update_classes(order, cls, length)
        length *= 2
    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))