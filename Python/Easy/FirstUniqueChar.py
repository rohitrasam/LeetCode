"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""


def firstUniqChar(s: str) -> int:

    counts = {}
    for idx in range(len(s)):
        if s[idx] in counts:
            counts[s[idx]][1] += 1
        else:
            counts[s[idx]] = [idx, 1]
    
    for key in counts:
        if counts[key][1] == 1:
            return counts[key][0]

    return -1

    

if __name__ == '__main__':
    string = input()

    print(firstUniqChar(string))