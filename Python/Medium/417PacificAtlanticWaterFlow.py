# https://leetcode.com/problems/pacific-atlantic-water-flow/description/


from typing import List, Set, Tuple


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    rows, cols = len(heights), len(heights[0])

    pac: Set[Tuple[int]] = set() 
    atl: Set[Tuple[int]] = set()

    def dfs(row: int, col: int, visit: Set[Tuple[int]], prevHeight: int) -> None:
        if ((row, col) in visit or
            row < 0 or col < 0 or row == rows or col == cols or
            heights[row][col] < prevHeight):
            return
        
        visit.add((row, col))
        dfs(row+1, col, visit, heights[row][col])
        dfs(row-1, col, visit, heights[row][col])
        dfs(row, col+1, visit, heights[row][col])
        dfs(row, col-1, visit, heights[row][col])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows-1, c, atl, heights[rows-1][c])

    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols-1, atl, heights[r][cols-1])
    
    res: List[Tuple[int]] = []
    for r in range(rows):
        for c in range(cols):
            if (r, c) in pac and (r, c) in atl:
                res.append((r, c))
    
    return res

if __name__ == '__main__':

    case = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacificAtlantic(case))

    case = [[1]]
    print(pacificAtlantic(case))


