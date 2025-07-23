"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""


""" My Solution """

# def longestSubstring(s: str) -> int:
#     if not s:
#         return 0
    
#     mx = 1
#     i = 0
#     j = i+1
#     substr = {s[i]}
#     while i < len(s)-1:
#         if s[j] in substr:
#             i += 1
#             j = i + 1
#             substr = {s[i]}
#         else:
#             substr.add(s[j])
#             j += 1
#             if mx < len(substr):
#                 mx = len(substr)
#         if j >=len(s):
#             i += 1
#             j = i+1

#     return mx


""" Least space """
# from collections import defaultdict

# def longestSubstring(s: str) -> int:
#         l, res = 0, 0
#         di = defaultdict()
#         for i, v in enumerate(s):
#             if v in di and di[v] >= l:
#                 l = di[v] + 1
#             else:
#                 res = max(i - l + 1, res)
#             di[v] = i
        
#         return res

""" Least Time """
def longestSubstring(s: str) -> int:
        n = len(s)
        maxLength = 0
        charIndex = [-1] *128
        left = 0

        for i in range (n):
            if charIndex[ord(s[i])] >= left:
                left = charIndex[ord(s[i])] + 1
            charIndex[ord(s[i])] = i
            maxLength = max(maxLength, i - left+1)

        return maxLength


if __name__ == '__main__':

    string = input()

    print(longestSubstring(string))
