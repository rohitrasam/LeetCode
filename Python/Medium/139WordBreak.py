# https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (i + len(word) <= len(s)) and s[i:i+len(word)] == word:
                dp[i] = dp[i+len(word)]
            if dp[i]:
                break
    
    return dp[0]


if __name__ == '__main__':

    case = "leetcode", ["leet","code"]
    print(wordBreak(*case))
    case = "applepenapple", ["apple","pen"]
    print(wordBreak(*case))
    case = "catsandog", ["cats","dog","sand","and","cat"]
    print(wordBreak(*case))
