# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=problem-list-v2&envId=backtracking


def smallestNumber(pattern: str) -> str:

    res, stack = [], []

    for i in range(len(pattern) + 1):
        stack.append(str(i + 1))

        while stack and (i == len(pattern) or pattern[i] == "I"):
            res.append(stack.pop())
        
    return "".join(res)

if __name__ == '__main__':

    case = "IIIDIDDD"
    print(smallestNumber(case))
    case = "DDD"
    print(smallestNumber(case))
