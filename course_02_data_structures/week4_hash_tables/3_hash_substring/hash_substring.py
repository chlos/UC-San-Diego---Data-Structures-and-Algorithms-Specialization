# python3

import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences_naive(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def hash_func(s, prime=1000000007, mult=263):
    ans = 0
    for c in reversed(s):
        ans = (ans * mult + ord(c)) % prime
    return ans


def precompute_hashes(text, pattern_len, p, x):
    H = [0] * (len(text) - pattern_len + 1)
    s = text[-pattern_len:]
    H[len(text) - pattern_len] = hash_func(s, p, x)
    y = 1
    for i in range(1, pattern_len + 1):
        y = (y * x) % p
    for i in reversed(range(len(text) - pattern_len)):
        pre_hash = x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])
        while(pre_hash < 0):
            pre_hash += p
        H[i] = pre_hash % p
    return H


def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randint(1, p)
    phash = hash_func(pattern, p, x)
    H = precompute_hashes(text, len(pattern), p, x)
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if phash == H[i] and text[i:i + len(pattern)] == pattern
    ]


def test():
    p = 'aba'
    s = 'abacaba'
    res = get_occurrences(p, s)
    res_exp = [0, 4]
    print(f'p: {p} ; text: {s} ; res: {res} (expected: {res_exp})')
    assert res == res_exp

    print('OK')


if __name__ == '__main__':
    # test()
    print_occurrences(get_occurrences(*read_input()))