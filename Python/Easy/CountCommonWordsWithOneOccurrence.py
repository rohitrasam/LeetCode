# https://leetcode.com/problems/count-common-words-with-one-occurrence/description/?envType=problem-list-v2&envId=hash-table


from collections import Counter
from typing import List


def countWords(words1: List[str], words2: List[str]) -> int:
    c1 = Counter(words1)
    c2 = Counter(words2)
    count = 0

    for word in c1:
        if word in c2 and c1[word] == c2[word] == 1:
            count += 1
    
    return count

if __name__ == '__main__':

    case = ["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]
    print(countWords(*case))
    case = ["b","bb","bbb"], ["a","aa","aaa"]
    print(countWords(*case))
    case = ["a","ab"], ["a","a","a","ab"]
    print(countWords(*case))
