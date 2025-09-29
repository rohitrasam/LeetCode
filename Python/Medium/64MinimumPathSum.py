# https://leetcode.com/problems/minimum-path-sum/description/?envType=problem-list-v2&envId=dynamic-programming




from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    
    dist = [[0] * len(grid[0]) for _ in range(len(grid))]
    dist[-1][-1] = grid[-1][-1]

    for r in range(len(grid) - 2, -1, -1):
        dist[r][-1] = grid[r][-1] + dist[r+1][-1]
        
    for c in range(len(grid[0]) - 2, -1, -1):
        dist[-1][c] = grid[-1][c] + dist[-1][c+1]
    
    
    for r in range(len(grid) - 2,  -1, -1):
        for c in range( len(grid[0]) - 2,  -1, -1):
            dist[r][c] = grid[r][c] + min(dist[r+1][c], dist[r][c+1])
    
    return dist[0][0]


if __name__ == '__main__':

    case = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(case))
    case = [[1,2,3],[4,5,6]]
    print(minPathSum(case))
    case = [[1,3,1,1],[1,2,1,1],[1,4,1,5],[1,3,4,3]]
    print(minPathSum(case))