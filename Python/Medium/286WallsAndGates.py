# Locked: https://leetcode.com/problems/walls-and-gates/description/
# Free: https://neetcode.io/problems/islands-and-treasure


from collections import deque
from typing import Deque, List, Set, Tuple


def islandsAndTreasure(grid: List[List[int]]) -> None:

    """ Neetcode Solution """

    q: Deque[Tuple[int]] = deque()
    visited: Set[Tuple[int]] = set()
    rows, cols = len(grid), len(grid[0])


    def addCell(r: int, c: int) -> None:
        if(min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == -1):
            return
        
        visited.add((r, c))
        q.append((r, c))


    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                q.append((row, col))
                visited.add((row, col))

    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            addCell(r+1, c)
            addCell(r-1, c)
            addCell(r, c+1)
            addCell(r, c-1)
        
        dist += 1


if __name__ == '__main__':

    case = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    islandsAndTreasure(case)
    print(case)
    case = [[0,-1],[2147483647,2147483647]]
    islandsAndTreasure(case)
    print(case)