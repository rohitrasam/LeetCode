# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/?envType=daily-question&envId=2025-01-06

from typing import List


def minOperations(boxes: str) -> List[int]:
    n = len(boxes)
    ans = [0] * n

    # for i in range(n):
    #     if boxes[i] == '1':
    #         for j in range(n):
    #             ans[j] += abs(j-i)
    
    ballsToLeft = movesToLeft = ballsToRight = movesToRight = 0

    for i in range(n):
        ans[i] += movesToLeft
        ballsToLeft += int(boxes[i])
        movesToLeft += ballsToLeft

        j = n - i - 1
        ans[j] += movesToRight
        ballsToRight += int(boxes[j])
        movesToRight += ballsToRight

    return ans

if __name__ == '__main__':
    case1 = "110"
    case2 = "001011"
    case3 = "001101"

    print(minOperations(case1))
    print(minOperations(case2))
    print(minOperations(case3))