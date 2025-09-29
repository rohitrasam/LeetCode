# https://leetcode.com/problems/unique-paths-ii/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1:
        return 0

    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    ways = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

    for r in range(rows):
        if obstacleGrid[r][0] == 1:
            break
        ways[r][0] = 1

    for c in range(cols):
        if obstacleGrid[0][c] == 1:
            break
        ways[0][c] = 1

    for r in range(1, rows):
        for c in range(1, cols):
            if obstacleGrid[r][c] == 1:
                continue

            ways[r][c] = ways[r - 1][c] + ways[r][c - 1]

    return ways[rows - 1][cols - 1]


if __name__ == "__main__":
    case = [[0, 1, 0, 0]]
    print(uniquePathsWithObstacles(case))

    case = [[0], [0]]
    print(uniquePathsWithObstacles(case))
    case = [[0, 0]]
    print(uniquePathsWithObstacles(case))
    case = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(uniquePathsWithObstacles(case))
    case = [[0, 1], [0, 0]]
    print(uniquePathsWithObstacles(case))
    case = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    print(uniquePathsWithObstacles(case))
    case = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(uniquePathsWithObstacles(case))
