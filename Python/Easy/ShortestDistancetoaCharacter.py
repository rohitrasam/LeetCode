# https://leetcode.com/problems/shortest-distance-to-a-character/description/?envType=problem-list-v2&envId=two-pointers

from typing import List


def shortestToChar(s: str, c: str) -> List[int]:
    n = len(s)
    ans = [n] * n
    l = r = 0

    while r < n:
        if s[r] != c:
            if s[l] == c:
                ans[r] = min(ans[r], abs(l - r))
            r += 1
        else:
            ans[l] = min(ans[l], abs(l - r))
            if r == l:
                r += 1
            else:
                l += 1
    
    return ans

if __name__ == '__main__':

    case = "loveleetcode", "e"
    print(shortestToChar(*case))
    case = "geeksforgeeks", "g"
    print(shortestToChar(*case))
    case = "aaab", "b"
    print(shortestToChar(*case))
