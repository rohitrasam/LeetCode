# https://leetcode.com/problems/baseball-game/

from typing import List

def calPoints(operations: List[str]) -> int:
    stack = []

    for op in operations:
        if op not in '+DC':
            stack.append(int(op))
        elif stack:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2*stack[-1])
            elif op == 'C':
                stack.pop()
    
    return sum( stack)



if __name__ == '__main__':
    case1 = ["5","2","C","D","+"]
    case2 = ["5","-2","4","C","D","9","+","+"]
    case3 = ["1","C"]

    print(calPoints(case1))
    print(calPoints(case2))
    print(calPoints(case3))