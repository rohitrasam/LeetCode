# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75


def mergeAlternately(self, word1: str, word2: str) -> str:
    w1 = w2 = 0
    ans = ""

    while w1 < len(word1) and w2 < len(word2):
        ans += word1[w1] + word2[w2]
        w1 += 1
        w2 += 1

    while w1 < len(word1):
        ans += word1[w1]
        w1 += 1

    while w2 < len(word2):
        ans += word2[w2]
        w2 += 1
    
    return ans