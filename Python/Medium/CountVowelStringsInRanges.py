# https://leetcode.com/problems/count-vowel-strings-in-ranges/submissions/1495303765/?envType=daily-question&envId=2025-01-02
from typing import List


def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    
    ans = [0] * len(queries)
    prefixSum = [0] * len(words)
    vowels = set('aeiou')

    total = 0
    for idx, word in enumerate(words):
        if word[0] in vowels and word[-1] in vowels:
           total += 1
        prefixSum[idx] = total

    for idx, query in enumerate(queries):
        ans[idx] = prefixSum[query[1]] - (0 if query[0] == 0 else prefixSum[query[0]-1])

    return ans


if __name__ == '__main__':
    case1 = ["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]
    case2 = ["a","e","i"], [[0,2],[0,1],[2,2]]
    case3 = ["norugjhgwqxrdrihwtwdfgi","ykywlzmiplhhvwpbvimczuzecl","rqindmyp","pkzwttxpyrjfyhmlhehjd"], [[1,2],[1,2],[3,3],[0,1],[0,0],[2,3],[0,2],[2,2],[1,1],[2,2],[0,2],[0,1],[2,3],[2,3],[2,2],[1,1],[2,2],[3,3],[3,3],[1,2],[1,3],[1,3],[3,3],[0,0],[0,3],[3,3],[3,3],[3,3],[3,3],[0,2],[2,3]]
    print(vowelStrings(*case1))
    print(vowelStrings(*case2))
    print(vowelStrings(*case3))