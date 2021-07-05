# python3
import sys


def KMPSearch(pat, txt):
    result = []

    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * M
    # index for pat[]
    j = 0

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    # index for txt[]
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            result.append(i - j)
            j = lps[j - 1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


def computeLPSArray(pat, M, lps):
    # length of the previous longest prefix suffix
    len = 0

    # lps[0] is always 0
    lps[0]
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example:
            # AAACAAAA and i = 7. The idea is similar to search step.
            if len != 0:
                len = lps[len - 1]
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = KMPSearch(pattern, text)
    print(" ".join(map(str, result)))