# https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=problem-list-v2&envId=two-pointers


def reverseWords(s: str) -> str:
    s = list(map(list, s.split()))

    for idx, word in enumerate(s):
        left, right = 0, len(word)-1

        while left <= right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        s[idx] = ''.join(word)
    
    return ' '.join(s)

if __name__ == '__main__':

    case = "Let's take LeetCode contest"
    print(reverseWords(case))
    case = "Mr Ding"
    print(reverseWords(case))
