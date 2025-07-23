# Question: https://leetcode.com/problems/generate-parentheses/description/

from typing import List

def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []

    def backtrack(open, close):
        if open == close == n:
            res.append("".join(stack))
        
        if open < n:
            stack.append("(")
            backtrack(open+1, close)
            stack.pop()
        
        if close < open:
            stack.append(")")
            backtrack(open, close+1)
            stack.pop()
    
    backtrack(0, 0)
    return res

if __name__ == '__main__':

    case1 = 3
    case2 = 1
    case3 = 4
    case4 = 2
    
    print(generateParenthesis(case1))
    print(generateParenthesis(case2))
    print(generateParenthesis(case3))
    print(generateParenthesis(case4))
