# https://leetcode.com/problems/triangle/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    
    """ My Solution """
    # if len(triangle) == 1:
    #     return triangle[0][0]

    # rows = len(triangle)
    # dp: List[List[int]] = [[float("inf")]* rows for n in range(rows)]
    # dp[0][0] = triangle[0][0]
    # dp[1][0] = dp[0][0] + triangle[1][0]
    # dp[1][1] = dp[0][0] + triangle[1][1]

    # for row in range(1, rows-1):
    #     cols = len(triangle[row])
    #     for col in range(cols):    
    #         dp[row+1][col] = min(dp[row][col] + triangle[row+1][col], dp[row+1][col])
    #         dp[row+1][col+1] = min(dp[row][col] + triangle[row+1][col+1], dp[row+1][col+1])
    
    # return min(dp[rows-1])

    """ Leetcode Solution """
    for row in range(len(triangle) -2, -1, -1):
        for col in range(row+1):
            triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
    
    return triangle[0][0]

if __name__ == '__main__':

    case = [[2],[3,4]]
    print(minimumTotal(case))
    case = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(minimumTotal(case))
    case = [[-10]]
    print(minimumTotal(case))
    case = [[3], [6,5], [4,1,3]]
    print(minimumTotal(case))