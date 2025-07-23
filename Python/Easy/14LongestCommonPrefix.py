# https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return prefix
        prefix += first[i]
    return prefix


if __name__ == '__main__':
    strs = input().split()

    print(longestCommonPrefix(strs))