# https://leetcode.com/problems/number-of-islands/description/


from typing import List, Set, Tuple


def numIslands(grid: List[List[str]]) -> int:
    """ Neetcode Solution """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])

    visit: Set[Tuple[int]] = set()
    islands = 0
    directions = [[1, 0,], [-1, 0], [0, 1], [0, -1]]

    def bfs(r: int, c: int):
        q: List[Tuple[int]] = []
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.pop(0)
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and 
                    c in range(cols) and 
                    grid[r][c] == "1" and
                    (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1

    return islands

if __name__ == '__main__':

    
    case = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands(case))
    case = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(numIslands(case))
