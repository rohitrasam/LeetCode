from typing import List

def isPalindrome(string: str) -> bool:
    return string == string[::-1]

def validPalindrome(s: str) -> bool:

    if isPalindrome(s):
        return True
    
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            skipL, skipR = s[l+1:r+1], s[l:r]
            return isPalindrome(skipL) or isPalindrome(skipR)
        l, r = l + 1, r - 1
    return True


if __name__ == '__main__':

    case1 = "aba"
    case2 = "abca"
    case3 = "abc"

    print(validPalindrome(case1))
    print(validPalindrome(case2))
    print(validPalindrome(case3))