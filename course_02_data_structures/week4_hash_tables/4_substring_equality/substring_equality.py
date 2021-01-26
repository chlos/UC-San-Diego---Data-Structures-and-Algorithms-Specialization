# python3

import sys
import random


class Solver:
    _prime_1 = 1000000007
    _prime_2 = 1000000009

    def __init__(self, s):
        self.s = s
        self.mult = random.randint(1, 10 ** 9)

        self.hashes_1 = self.precompute_hashes(self._prime_1)
        self.hashes_2 = self.precompute_hashes(self._prime_2)

        self.mods_1 = self.precompute_mods(self._prime_1)
        self.mods_2 = self.precompute_mods(self._prime_2)

    def precompute_hashes(self, prime):
        hashes = [None] * (len(self.s) + 1)
        hashes[0] = 0
        for i, s in enumerate(self.s, 1):
            hashes[i] = (hashes[i - 1] * self.mult + ord(s)) % prime
        return hashes

    def precompute_mods(self, prime):
        mods = [1] + [0] * len(self.s)
        for i in range(1, len(self.s) + 1):
            mods[i] = ((mods[i - 1] * self.mult) % prime + prime) % prime
        return mods

    def ask(self, a, b, s_len):
        a_h1 = (
            (self.hashes_1[a + s_len] - self.hashes_1[a] * self.mods_1[s_len]) % self._prime_1 + self._prime_1
        ) % self._prime_1
        a_h2 = (
            (self.hashes_2[a + s_len] - self.hashes_2[a] * self.mods_2[s_len]) % self._prime_2 + self._prime_2
        ) % self._prime_2

        b_h1 = (
            (self.hashes_1[b + s_len] - self.hashes_1[b] * self.mods_1[s_len]) % self._prime_1 + self._prime_1
        ) % self._prime_1
        b_h2 = (
            (self.hashes_2[b + s_len] - self.hashes_2[b] * self.mods_2[s_len]) % self._prime_2 + self._prime_2
        ) % self._prime_2

        if (a_h1 == b_h1) and (a_h2 == b_h2):
            return True
        else:
            return False


def main():
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for _ in range(q):
        a, b, s_len = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, s_len) else "No")


if __name__ == "__main__":
    main()