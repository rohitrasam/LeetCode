from typing import List
from collections import defaultdict

def isValidSudoku(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    sqrs = defaultdict(set)

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == ".":
                continue 
            if board[row][col] in rows[row] or board[row][col] in cols[col]or board[row][col] in sqrs[(row // 3, col // 3)]:
                return False
            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            sqrs[(row // 3, col // 3)].add(board[row][col])
    return True


if __name__ == '__main__':
    case1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    case2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    print(isValidSudoku(case1))
    print(isValidSudoku(case2))