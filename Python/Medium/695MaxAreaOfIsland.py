# https://leetcode.com/problems/max-area-of-island/description/

from typing import List, Set, Tuple


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """ My Soution: BFS """
    # visited: Set[Tuple[int]] = set()
    # rows, cols = len(grid), len(grid[0])
    # maxArea = 0

    # directions = [[1, 0,], [-1, 0], [0, 1], [0, -1]]


    # def bfs(row: int, col: int) -> int:
    #     area = 1
    #     q: List[Tuple[int]] = []
    #     q.append((row, col))
    #     visited.add((row, col))

    #     while q:
    #         r, c = q.pop(0)

    #         for dr, dc in directions:
    #             new_r, new_c = r + dr, c + dc

    #             if (new_r in range(rows) and 
    #                 new_c in range(cols) and
    #                 (new_r, new_c) not in visited and
    #                 grid[new_r][new_c] == 1):
    #                 q.append((new_r, new_c))
    #                 visited.add((new_r, new_c))
    #                 area += 1
        
    #     return area

    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 1:
    #             currArea = bfs(row, col)
    #             maxArea = max(maxArea, currArea)
    
    # return maxArea

    """ Leetcode Solution: DFS """
    rows, cols = len(grid), len(grid[0])
    maxArea = 0
    directions = [[1, 0,], [-1, 0], [0, 1], [0, -1]]

    def dfs(r: int, c: int) -> int:
        if (r < 0 or r >= rows) or (c < 0 or c >= cols) or grid[r][c] == 0:
            return 0 

        grid[r][c] = 0
        area = 0
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            area += dfs(new_r, new_c)
        
        return area + 1


    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                currArea = dfs(row, col)
                maxArea = max(maxArea, currArea)
    
    return maxArea



if __name__ == '__main__':

    case = [[1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]]
    print(maxAreaOfIsland(case))
    case = [[1,1,1,0,0],
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1]]
    print(maxAreaOfIsland(case))
    case = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(maxAreaOfIsland(case))
    case = [[0,0,0,0,0,0,0,0]]
    print(maxAreaOfIsland(case))
        
