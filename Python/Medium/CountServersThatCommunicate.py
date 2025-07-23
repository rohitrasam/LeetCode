# https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23

from typing import List


def countServers(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    rowCount = [0] * rows
    colCount = [0] * cols
    com_servers = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                rowCount[row] += 1
                colCount[col] += 1
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] and (rowCount[row] > 1 or colCount[col] > 1):
                com_servers += 1

    return com_servers

if __name__ == '__main__':

    case1 = [[1,0],
             [0,1]]
    case2 = [[1,0],
             [1,1]]
    case3 = [[1,1,0,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,0,1]]
    case4 = [[1,1,0,0],
             [0,0,0,0],
             [0,0,1,0],
             [0,0,1,1]]
    case5 = [[1,1,1,0],
             [0,0,1,0],
             [0,0,1,0],
             [0,0,0,1]]

    # print(countServers(case1))
    print(countServers(case2))
    print(countServers(case3))
    print(countServers(case4))
    print(countServers(case5))
