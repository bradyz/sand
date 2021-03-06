# Rearrange Description:
# Given a string, say "ddabcbd"
# Return a string sorted by frequency, then alpha
# Ex: "dddbbac"

import sys
from collections import Counter


def rearrange(a_str):
    a_list = list(a_str)
    count = Counter()

    for char in a_list:
        count[char] += 1

    freq = {}

    for c in count:
        if count[c] in freq:
            freq[count[c]].append(c)
        else:
            freq[count[c]] = [c]
    print(freq)

    result = ""

    for f in reversed(sorted(freq.keys())):
        for c in sorted(freq[f]):
            result += f * c

    return result

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        to_rea = line.strip("\n")
        res = rearrange(to_rea)
        print(res)
