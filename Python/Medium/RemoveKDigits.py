from typing import List


def removeKdigits(num: str, k: int) -> str:
    
    stack = []
    for char in num:
        while k > 0 and stack and stack[-1] > char:
            k -= 1
            stack.pop()
        stack.append(char)
    
    stack = stack[:len(stack) - k]
    res = "".join(stack).lstrip("0")
    return res if res else "0"


if __name__ == '__main__':

    case1 = "1432219", 3
    case2 = "10200", 1
    case3 = "10", 2

    print(removeKdigits(*case1))
    print(removeKdigits(*case2))
    print(removeKdigits(*case3))


