# https://leetcode.com/problems/valid-word/description/


from typing import Set


def isValid(word: str) -> bool:
    if len(word) < 3:
        return False
    
    vows: Set[str] = {"a", "e", "i", "o", "u"}
    v = False
    c = False

    for w in word:
        w = w.casefold()
        if not w.isalnum():
            return False
        if w.isalpha() and w in vows:
            v = True
        elif w.isalpha() and w not in vows:
            c = True
    
    return True if v and c else False



if __name__ == '__main__':

    case = "234Adas"
    print(isValid(case))

    case = "b3"
    print(isValid(case))

    case = "a3$e"
    print(isValid(case))
