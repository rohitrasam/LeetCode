# https://leetcode.com/problems/word-subsets/?envType=daily-question&envId=2025-01-10

from typing import List


def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    
    def count(word: str):
        ans = [0] * 26
        for letter in word:
            ans[ord(letter) - ord('a')] += 1
        return ans
    
    bmax = [0] * 26
    for substr in words2:
        for i, c in enumerate(count(substr)):
            bmax[i] = max(bmax[i], c)

    ans = []
    for word in words1:
        if all(x >= y for x, y in zip(count(word), bmax)):
            ans.append(word)

    return ans


if __name__ == '__main__':
    
    case1 = ["amazon","apple","facebook","google","leetcode"], ["e","o"]
    case2 = ["amazon","apple","facebook","google","leetcode"], ["l","e"]

    print(wordSubsets(*case1))
    print(wordSubsets(*case2))