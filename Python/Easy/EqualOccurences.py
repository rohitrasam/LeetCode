# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/?envType=problem-list-v2&envId=hash-table


from typing import Dict


def areOccurrencesEqual(s: str) -> bool:
    # count: Dict[str, int] = {}

    # for char in s:
    #     count[char] = count.get(char, 0) + 1
    
    # prev = count[s[0]]
    # for char in count:
    #     if count[char] == prev:
    #         prev = count[char]
    #     else:
    #         return False
    
    # return True

    count: Dict[str, int] = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    
    return len(set(count.values())) == 1


if __name__ == '__main__':

    case1 = "abacbc"
    case2 = "aaabb"

    print(areOccurrencesEqual(case1))    
    print(areOccurrencesEqual(case2))    