# https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-07

from typing import List


def stringMatching(words: List[str]) -> List[str]:

    ans = []

    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            substr = min(words[i], words[j], key=len)
            string = max(words[i], words[j], key=len)
            if substr == string:
                continue
            elif set(substr).issubset(string):
                ans.append(substr)

    return ans

if __name__ == '__main__':
    case1 = ["mass","as","hero","superhero"]
    case2 = ["leetcode","et","code"]
    case3 = ["blue","green","bu"]

    print(stringMatching(case1))
    print(stringMatching(case2))
    print(stringMatching(case3))