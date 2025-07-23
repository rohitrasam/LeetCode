# Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


from typing import List


def evalRPN(tokens: List[str]) -> int:
    
    stack = []
    ops = {"+", "-", "/", "*"}

    for token in tokens:
        if token not in ops:
            stack.append(token)
        else:
            right = int(stack.pop())
            left = int(stack.pop())
            if token == "+":
                ans = left + right
            if token == "-":
                ans = left - right
            if token == "/":
                ans = int(left / right)
            if token == "*":
                ans = left * right
            stack.append(ans)
    
    return stack[0]



if __name__ == '__main__':

    case1 = ["2","1","+","3","*"]
    case2 = ["4","13","5","/","+"]
    case3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    print(evalRPN(case1))
    print(evalRPN(case2))
    print(evalRPN(case3))
