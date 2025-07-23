# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/?envType=daily-question&envId=2025-01-13


from typing import Counter


def minimumLength(s: str) -> int:

    # char_freq = Counter(s)

    # delete_char = 0

    # for freq in char_freq.values():
    #     if freq % 2 == 1:
    #         delete_char += freq - 1
    #     else:
    #         delete_char += freq - 2
    
    # return len(s) - delete_char

    char_freq = [0] * 26

    for char in s:
        char_freq[ord(char) - ord('a')] += 1

    del_char = 0
    for freq in char_freq:
        if freq == 0:
            continue
        if freq % 2 == 1:
            del_char += freq - 1
        else:
            del_char += freq - 2
        
    return len(s) - del_char

if __name__ == '__main__':

    case1 = "abaacbcbb"
    case2 = "aa"

    print(minimumLength(case1))
    print(minimumLength(case2))