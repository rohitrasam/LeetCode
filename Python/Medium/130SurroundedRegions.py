# https://leetcode.com/problems/surrounded-regions/description/

from typing import List, Set, Tuple
import numpy as np

def solve(board: List[List[str]]) -> None:
    
    rows, cols = len(board), len(board[0])
    # visited: Set[Tuple[int]] = set()

    def dfs(row: int, col: int) -> None:
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            # (row, col) in visited or
            board[row][col] == "S" or
            board[row][col] == "X"):
            return
        # visited.add((row, col))
        board[row][col] = "S"
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)
        
    for r in range(rows):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][cols-1] =='O':
            dfs(r, cols-1)
    
    for c in range(cols):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[rows-1][c] =='O':
            dfs(rows-1, c)
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "S":
                board[r][c] = "O"
            elif board[r][c] == "O":
                board[r][c] = "X"


if __name__ == '__main__':

    case = [["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]]
    solve(case)
    print(np.array(case))

    case = [["O","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]]
    solve(case)
    print(np.array(case))

    case = [["O","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","O","X","X"]]
    solve(case)
    print(np.array(case))

    case = [["X"]]
    solve(case)
    print(np.array(case))

