# https://leetcode.com/problems/maximal-square/description/?envType=problem-list-v2&envId=dynamic-programming

from typing import Dict, List, Tuple


def maximalSquare(matrix: List[List[str]]) -> int:
    
    ROWS, COLS = len(matrix), len(matrix[0])
    cache: Dict[Tuple[int, int], int] = {}    


    def helper(r: int, c: int) -> int:
        if r >= ROWS or c >= COLS:
            return 0
        
        if (r, c) not in cache:
            down = helper(r+1,c)
            right = helper(r, c+1)
            diag = helper(r+1, c+1)
            cache[(r, c)] = 0

            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, diag)
        
        return cache[(r, c)]

    helper(0, 0)
    return max(cache.values())**2


if __name__ == '__main__':


    case = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximalSquare(case))
    case = [["0","1"],["1","0"]]
    print(maximalSquare(case))
    case = [["0"]]
    print(maximalSquare(case))
