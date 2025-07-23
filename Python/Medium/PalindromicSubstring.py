# https://leetcode.com/problems/palindromic-substrings/description/?envType=problem-list-v2&envId=dynamic-programming


def countSubstrings(s: str) -> int:
    
    """ Two Pointer """
    # res = 0

    # for i in range(len(s)):

    #     l = r = i
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         res += 1
    #         l -= 1
    #         r += 1
        
    #     l, r = i, i + 1
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         res += 1
    #         l -= 1
    #         r += 1

    # return res

    """ 2D - DP """
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = 0

    for i in range(n):
        dp[i][i] = True
        res += 1
    
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            res += 1

    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff

            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                res += 1
    
    return res


if __name__ == '__main__':

    case = "abc"
    print(countSubstrings(case))
    case = "aaa"
    print(countSubstrings(case))
    case = "racecar"
    print(countSubstrings(case))