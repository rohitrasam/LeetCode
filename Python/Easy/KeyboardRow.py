from typing import List

def findWords(words: List[str]) -> List[str]:
    row1 = set('qwertyuiop')
    row2 = set('asdfghjkl')
    row3 = set('zxcvbnm')

    res = []
    for word in words:
        row = []
        for char in word:
            if char.casefold() in row1:
                if not row or row[-1] == 1:
                    row.append(1)   
                else:
                    break
            if char.casefold() in row2:
                if not row or row[-1] == 2:
                    row.append(2)
                else:
                    break
            if char.casefold() in row3:
                if not row or row[-1] == 3:
                    row.append(3)   
                else:
                    break
        if len(row) == len(word):
            res.append(word)
    
    return res


if __name__ == '__main__':

    case1 = ["Hello","Alaska","Dad","Peace"]
    case2 = ["omk"]
    case3 = ["adsdf","sfd"]

    print(findWords(case1))
    print(findWords(case2))
    print(findWords(case3))