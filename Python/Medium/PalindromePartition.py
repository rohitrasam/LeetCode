# https://leetcode.com/problems/palindrome-partitioning/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def partition(s: str) -> List[List[str]]:
            
    res = []
    part = []

    def dfs(i: int) -> None:
        if i >= len(s):
            res.append(part[:])
            return
        for j in range(i, len(s)):
            if isPal(s, i, j):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()
           
         
    dfs(0)
    return res

def isPal(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == '__main__':

    case = "aab"
    print(partition(case))
    case = "aabaa"
    print(partition(case))
    case = "aabca"
    print(partition(case))
    case = "a"
    print(partition(case))