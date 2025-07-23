# https://leetcode.com/problems/longest-common-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming


def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0] * (len(text1) + 1) for _ in range(len(text2)+1)]

    for row in range(len(text2) - 1, -1, -1):
        for col in range(len(text1) - 1, -1, -1):
            if text2[row] == text1[col]:
                dp[row][col] = 1 + dp[row+1][col+1]
            else:
                dp[row][col] = max(dp[row+1][col], dp[row][col+1])
    
    return dp[0][0]

if __name__ == '__main__':

    # case = "ezupkr", "ubmrapg"
    # print(longestCommonSubsequence(*case))
    # case = "psnw", "vozsh"
    # print(longestCommonSubsequence(*case))
    # case = "bl", "yby"
    # print(longestCommonSubsequence(*case))
    case = "abcde", "ace"
    print(longestCommonSubsequence(*case))
    case = "abcde", "abf"
    print(longestCommonSubsequence(*case))
    case = "abc", "abc"
    print(longestCommonSubsequence(*case))
    case = "abc", "def"
    print(longestCommonSubsequence(*case))