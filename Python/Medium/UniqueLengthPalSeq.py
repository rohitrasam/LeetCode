# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04

def countPalindromicSubsequence(s: str) -> int:
    letters = set(s)
    ans = 0
    for letter in letters:
        start, end = s.index(letter), s.rindex(letter)
        between = set()
        for pivot in range(start+1, end):
            between.add(s[pivot])

        ans += len(between)

    return ans



if __name__ == '__main__':
    case1 = "aabca"
    case2 = "adc"
    case3 = "bbcbaba"

    # print(countPalindromicSubsequence(case1))
    # print(countPalindromicSubsequence(case2))
    print(countPalindromicSubsequence(case3))