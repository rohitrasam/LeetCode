# https://leetcode.com/problems/word-search/description/?envType=problem-list-v2&envId=backtracking



from typing import List


def exist(board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r: int, c: int, i: int):
            if i == len(word):
                return True
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] != word[i] or (r, c) in visited):
                return False
        
            visited.add((r, c))
            res = ( 
                    dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1)
                )
            visited.remove((r, c))
            return res
    
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == '__main__':

    case = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
    print(exist(*case))
    case = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"
    print(exist(*case))
    case = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"
    print(exist(*case))