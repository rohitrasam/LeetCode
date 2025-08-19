# https://leetcode.com/problems/different-ways-to-add-parentheses/description/


from typing import List


def diffWaysToCompute(expression: str) -> List[int]:
    ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}

    def bt(left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            op = expression[i]
            if op in ops:
                nums1 = bt(left, i - 1)
                nums2 = bt(i + 1, right)
                for n1 in nums1:
                    for n2 in nums2:
                        res.append(ops[op](n1, n2))

        if res == []:
            res.append(int(expression[left:right+1]))
        return res

    return bt(0, len(expression) - 1)


if __name__ == "__main__":
    case = "2-1-1"
    print(diffWaysToCompute(case))
    case = "2*3-4*5"
    print(diffWaysToCompute(case))
