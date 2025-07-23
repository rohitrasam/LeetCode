# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=backtracking


from typing import List


def letterCombinations(digits: str) -> List[str]:
    mapping = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    res = []


    def back(i: int, curStr: str) -> None:
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in mapping[digits[i]]:
            back(i+1, curStr + c)
        
    if digits:
        back(0, "")
    
    return res
        


if __name__ == '__main__':

    case = "23"
    print(letterCombinations(case))
    case = ""
    print(letterCombinations(case))
    case = "2"
    print(letterCombinations(case))