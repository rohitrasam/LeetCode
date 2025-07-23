# https://leetcode.com/problems/clumsy-factorial/?envType=problem-list-v2&envId=stack

def clumsy(n: int) -> int:

    stack = []
    ops = "*/+-"
    op = 0
    for i in range(n, 0, -1):
        if stack:
            if ops[op] == "*":
                last = stack.pop()
                stack.append(last*i)
            elif ops[op] == "/":
                last = stack.pop()
                stack.append(int(last / i))
            elif ops[op] == "+":
                last = stack.pop()
                stack.append(last+i)
            elif ops[op] == "-":
                stack.append(-i)
            op = (op + 1) % 4
        else:
            stack.append(i)

    for nums in stack[1:]:
        stack[0] += nums

    return stack[0]


if __name__ == '__main__':

    case = 4
    print(clumsy(case))
    case = 10
    print(clumsy(case))
    case = 15
    print(clumsy(case))