# Question: https://leetcode.com/problems/longest-palindromic-substring/description/


def longestPalindrome(s: str) -> str:
    """ Two Pointer - Neetcode """
    # res = ""
    # resLen = 0

    # for i in range(len(s)):

    #     # odd length
    #     l = r = i
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if(r - l + 1) > resLen:
    #             res = s[l:r+1]
    #             resLen = r - l + 1
    #         l -= 1
    #         r += 1

    #     # even length
    #     l, r = i, i+1
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if(r - l + 1) > resLen:
    #             res = s[l:r+1]
    #             resLen = r - l + 1
    #         l -= 1
    #         r += 1

    # return res        

    """ 2D - DP Editorial """
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    ans = [0, 0]

    for i in range(n):
        dp[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = [i, i+1]

    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff

            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                ans = [i, j]

    return s[ans[0]:ans[1]+1]

if __name__ == '__main__':

    case1 = "babad"
    case2 = "cbbd"

    print(longestPalindrome(case1))
    print(longestPalindrome(case2))