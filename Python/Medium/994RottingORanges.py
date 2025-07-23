# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque
from typing import Deque, List, Set, Tuple

""" - Start by queueing up all the rotten oranges
    - Start bfs from all the rotten oranges
    - After traversing through the queue increase time by 1
"""


def orangesRotting(grid: List[List[int]]) -> int:
    
    q: Deque[Tuple[int]] = deque()
    visited: Set[Tuple[int]] = set()
    rows, cols = len(grid), len(grid[0])

    def bfs(row: int, col: int) -> None:
        if ((row >= rows or row < 0) or 
            (col >= cols or col < 0) or 
            ((row, col) in visited) or 
            grid[row][col] == 0):
            return
        q.append((row, col))
        visited.add((row, col))

    # queue up all rotten mangoes
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 2:
                q.append((x, y))
                visited.add((x, y))

    # traverse through the queue for bfs
    time = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = 2
            bfs(r+1, c)
            bfs(r-1, c)
            bfs(r, c+1)
            bfs(r, c-1)
        if q:
            time += 1
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                return -1

    return time
    
if __name__ == '__main__':
    case = [[2,1,1],
            [1,1,0],
            [0,1,1]]
    print(orangesRotting(case))
    
    case = [[2,1,1],
            [0,1,1],
            [1,0,1]]
    print(orangesRotting(case))
    
    case = [[0,2]]
    print(orangesRotting(case))