# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=problem-list-v2&envId=two-pointers


def reverseVowels(s: str) -> str:
    s = list(s)
    left, right = 0, len(s) - 1

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    while left <= right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        # if s[left] in vowels and s[right] in vowels:
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return ''.join(s)

if __name__ == '__main__':
    
    # case = "IceCreAm"
    # print(reverseVowels(case))    
    # case = "leetcode"
    # print(reverseVowels(case))
    # case = ".a"
    # print(reverseVowels(case))
    case = " "
    print(reverseVowels(case))