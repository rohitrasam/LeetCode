# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/?envType=problem-list-v2&envId=hash-table


from collections import Counter


def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    count1 = [0] * 26
    count2 = [0] * 26

    for let in word1:
        count1[ord(let) - ord('a')] += 1
    for let in word2:
        count2[ord(let) - ord('a')] += 1

    for idx in range(len(count1)):
        if abs(count1[idx] - count2[idx]) > 3:
            return False
    
    return True

if __name__ == '__main__':
    
    case = "aaaa", "bccb"
    print(checkAlmostEquivalent(*case))
    case = "aaaa", "bbbba"
    print(checkAlmostEquivalent(*case))
    case = "abcdeef", "abaaacc"
    print(checkAlmostEquivalent(*case))
    case = "cccddabba", "babababab"
    print(checkAlmostEquivalent(*case))
