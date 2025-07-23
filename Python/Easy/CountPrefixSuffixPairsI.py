# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08

from typing import List

def isPrefixAndSuffix(word1: str, word2: str):
    return word1 == word2[:len(word1)] == word2[-len(word1):]

def countPrefixSuffixPairs(words: List[str]) -> int:
    
    count = 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i < j and isPrefixAndSuffix(words[i], words[j]):
                count += 1
    
    return count


if __name__ == '__main__':

    case1 = ["a","aba","ababa","aa"]
    case2 = ["pa","papa","ma","mama"]
    case3 = ["abab","ab"]

    print(countPrefixSuffixPairs(case1))
    print(countPrefixSuffixPairs(case2))
    print(countPrefixSuffixPairs(case3))
