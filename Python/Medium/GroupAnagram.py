from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = {}
    for st in strs:
        count = [0] * 26
        for char in st:
            count[ord(char) - ord('a')] += 1
        if tuple(count) not in ans:
            ans[tuple(count)] = [st]
        else:
            ans[tuple(count)].append(st)
    
    return ans.values()


if __name__ == '__main__':

    case1 = ["eat","tea","tan","ate","nat","bat"]
    case2 = [""]
    case3 = ["a"]
    print(groupAnagrams(case1))
    print(groupAnagrams(case2))
    print(groupAnagrams(case3))