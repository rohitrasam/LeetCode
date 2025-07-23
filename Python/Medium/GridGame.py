# https://leetcode.com/problems/grid-game/description/?envType=daily-question&envId=2025-01-21

from typing import List

def gridGame(grid: List[List[int]]) -> int:

    cols = len(grid[0])

    firstSum = sum(grid[0])
    secondSum = 0
    minSum = float('inf')

    for col in range(cols):
        firstSum -= grid[0][col]
        minSum = min(minSum, max(firstSum, secondSum))
        secondSum += grid[1][col]
    
    return minSum

if __name__ == '__main__':
    
    case1 = [[2,5,4],[1,5,1]]
    case2 = [[3,3,1],[8,5,2]]
    case3 = [[1,3,1,15],[1,3,3,1]]

    print(gridGame(case1))
    print(gridGame(case2))
    print(gridGame(case3))