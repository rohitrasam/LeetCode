# https://leetcode.com/problems/path-with-maximum-gold/description/?envType=problem-list-v2&envId=backtracking


from typing import List, Set, Tuple


def getMaximumGold(grid: List[List[int]]) -> int:
    """Using hashset"""
    # rows, cols = len(grid), len(grid[0])

    # def dfs(r: int, c: int, visit: Set[Tuple[int, int]]):
    #     if (
    #         min(r, c) < 0
    #         or r == rows
    #         or c == cols
    #         or grid[r][c] == 0
    #         or (r, c) in visit
    #     ):
    #         return 0

    #     visit.add((r, c))
    #     res = grid[r][c]
    #     neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
    #     for nr, nc in neighbors:
    #         res = max(res, grid[r][c] + dfs(nr, nc, visit))

    #     visit.add((r, c))
    #     return res

    # res = 0
    # for i in range(rows):
    #     for j in range(cols):
    #         res = max(res, dfs(i, j, set()))

    # return res

    """ Without using hashset """
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int):
        if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
            return 0

        tmp = grid[r][c]
        grid[r][c] = 0
        res = 0
        neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in neighbors:
            res = max(res, tmp + dfs(nr, nc))

        grid[r][c] = tmp
        return res

    res = 0
    for i in range(rows):
        for j in range(cols):
            res = max(res, dfs(i, j))

    return res


if __name__ == "__main__":
    case = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    print(getMaximumGold(case))
    case = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    print(getMaximumGold(case))
    case = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 1, 20]]
    print(getMaximumGold(case))
