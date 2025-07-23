# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/?envType=daily-question&envId=2025-01-12

from typing import List


def canBeValid(s: str, locked: str) -> bool:
    # if len(s) % 2 != 0:
    #     return False
    
    # openBracks: List[str] = []
    # unlocked: List[str] = []


    # for idx in range(len(s)):
    #     if locked[idx] == "0":
    #         unlocked.append(idx)
    #     elif s[idx] == "(":
    #         openBracks.append(idx)
    #     elif s[idx] == ")":
    #         if openBracks:
    #             openBracks.pop()
    #         elif unlocked:
    #             unlocked.pop()
    #         else:
    #             return False
        
    # while openBracks and unlocked and openBracks[-1] < unlocked[-1]:
    #     openBracks.pop()
    #     unlocked.pop()

    # if openBracks:
    #     return False
    
    # return True


    length = len(s)
    # If length of string is odd, return false.
    if length % 2 == 1:
        return False
    open_brackets = 0
    unlocked_count = 0
    # Iterate through the string to handle '(' and ')'.
    for i in range(length):
        if locked[i] == "0":
            unlocked_count += 1
        elif s[i] == "(":
            open_brackets += 1
        elif s[i] == ")":
            if open_brackets > 0:
                open_brackets -= 1
            elif unlocked_count > 0:
                unlocked_count -= 1
            else:
                return False

    # Match remaining open brackets with unlocked characters.
    balance_count = 0
    for i in range(length - 1, -1, -1):
        if locked[i] == "0":
            balance_count -= 1
            unlocked_count -= 1
        elif s[i] == "(":
            balance_count += 1
            open_brackets -= 1
        elif s[i] == ")":
            balance_count -= 1
        if balance_count > 0:
            return False
        if unlocked_count == 0 and open_brackets == 0:
            break

    if open_brackets > 0:
        return False

    return True

if __name__ == '__main__':

    case1 = "))()))", "010100"
    case2 = "()()", "0000"
    case3 = ")", "0"
    case4 = "))()))", "010110"
    case5 = "(()())", "010100"
    case6 = "()))", "0010"

    print(canBeValid(*case1))
    # print(canBeValid(*case2))
    # print(canBeValid(*case3))
    print(canBeValid(*case4))
    print(canBeValid(*case5))
    print(canBeValid(*case6))