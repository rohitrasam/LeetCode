# https://leetcode.com/problems/make-number-of-distinct-characters-equal/description/

from string import ascii_lowercase
from collections import Counter
from typing import Dict

def isItPossible(word1: str, word2: str) -> bool:
    frq1: Dict[str, int] = Counter(word1)
    frq2: Dict[str, int] = Counter(word2)

    def swap(frq: Dict[str, int], c1: str, c2: str):
        frq[c1] += 1
        frq[c2] -= 1
        if frq[c2] == 0:
            frq.pop(c2)

    a = ord('a')

    for ch1 in ascii_lowercase:
        for ch2 in ascii_lowercase:
            if ch1 not in frq1 or ch2 not in frq2:
                continue

            swap(frq1, ch2, ch1)
            swap(frq2, ch1, ch2)

            if len(frq1) == len(frq2):
                return True

            swap(frq1, ch1, ch2)
            swap(frq2, ch2, ch1)
    
    return False



if __name__ == '__main__':

    case1 = "ac", "b"
    case2 = "abcc", "aab"
    case3 = "abcde", "fghij"

    print(isItPossible(*case1))
    print(isItPossible(*case2))    
    print(isItPossible(*case3))