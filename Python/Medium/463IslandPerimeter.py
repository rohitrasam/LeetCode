# https://leetcode.com/problems/island-perimeter/description/

from typing import List, Set, Tuple


def islandPerimeter(grid: List[List[int]]) -> int:
    # start = [0, 0]
    # peri = 0
    # rows, cols = len(grid), len(grid[0])
    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 1:
    #             start = [row, col]
    #             break

    # visited: Set[Tuple[int, int]] = set()

    # def dfs(r: int, c: int):
    #     if (r, c) in visited:
    #         return

    #     if r < 0 or r == rows or c < 0 or c >= cols or grid[r][c] == 0:
    #         nonlocal peri
    #         peri += 1
    #         return

    #     visited.add((r, c))
    #     dfs(r, c + 1)
    #     dfs(r, c - 1)
    #     dfs(r + 1, c)
    #     dfs(r - 1, c)

    # dfs(*start)
    # return peri

    start = [0, 0]
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                start = [row, col]
                break

    visited: Set[Tuple[int, int]] = set()

    def dfs(r: int, c: int) -> int:
        if (r, c) in visited:
            return 0

        if r < 0 or r == rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 1

        visited.add((r, c))
        res = dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
        return res

    return dfs(*start)
    # return peri


if __name__ == "__main__":
    case = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(islandPerimeter(case))
    case = [[1]]
    print(islandPerimeter(case))
    case = [[1, 0]]
    print(islandPerimeter(case))
