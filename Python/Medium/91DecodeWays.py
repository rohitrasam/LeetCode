# https://leetcode.com/problems/decode-ways/description/?envType=problem-list-v2&envId=dynamic-programming


def numDecodings(s: str) -> int:
    
    """ Bottom Up Approach DP """
    dp = {len(s): 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
        
        if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            dp[i] += dp[i+2]

    return dp[0]


    """ Recursive DP """

    # dp = {len(s): 1}
    
    # def dfs(i: int) -> int:
    #     if i in dp:
    #         return dp[i]
    #     if s[i] == "0":
    #         return 0
        
    #     res = dfs(i + 1)
    #     if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
    #         res += dfs(i + 2)

    #     dp[i] = res
    #     return res
    
    # return dfs(0)

if __name__ == '__main__':

    case = "12"
    print(numDecodings(case))
    case = "226"
    print(numDecodings(case))
    case = "06"
    print(numDecodings(case))