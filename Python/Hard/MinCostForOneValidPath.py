# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=daily-question&envId=2025-01-18

import heapq
from typing import List

""" Dynamic Programming """
"""
def minCost(grid: List[List[int]]) -> int:

    rows, cols = len(grid), len(grid[0])
    minChanges = {(row, col): float("inf") for row in range(rows) for col in range(cols)}
    minChanges[(0, 0)] = 0
    while True:
        prev_state = minChanges.copy()

        for row in range(rows):
            for col in range(cols):
                if row > 0:
                    minChanges[(row, col)] = min(minChanges[(row, col)], 
                                                 minChanges[(row-1, col)] + (0 if grid[row-1][col] == 3 else 1))
                if col > 0:
                    minChanges[(row, col)] = min(minChanges[(row, col)], 
                                                 minChanges[(row, col-1)] + (0 if grid[row][col-1] == 1 else 1))
        
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if row < rows - 1:
                    minChanges[(row, col)] = min(minChanges[(row, col)],
                                                 minChanges[(row+1, col)] + (0 if grid[row+1][col] == 4 else 1))
                if col < cols - 1:
                    minChanges[(row, col)] = min(minChanges[(row, col)],
                                                 minChanges[(row, col+1)] + (0 if grid[row][col+1] == 2 else 1))
            
        if prev_state == minChanges:
            break 

    return minChanges[(rows-1, cols-1)]
"""

""" Dijkstra's Algorithm """
"""
# def minCost(grid: List[List[int]]) -> int:
#     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
#     num_rows = len(grid)
#     num_cols = len(grid[0])

#     min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
#     min_cost[0][0] = 0
#     pq =  [(0, 0, 0)]

#     while pq:
#         cost, row, col = heapq.heappop(pq)

#         if min_cost[row][col] != cost:
#             continue

#         for d, (dx, dy) in enumerate(dirs):
#             new_row, new_col = row + dx, col + dy

#             if 0 <= new_row < num_rows and 0 <= new_col < num_cols:

#                 new_cost = cost + (d != grid[row][col] - 1)

#                 if min_cost[new_row][new_col] > new_cost:
#                     min_cost[new_row][new_col] = new_cost
#                     heapq.heappush(pq, (new_cost, new_row, new_col))
        
#     return min_cost[num_rows - 1][num_cols - 1]
"""

""" Breadth First Search """

def minCost(grid: List[List[int]]) -> int:
        #   (r, c)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_rows, num_cols =len(grid), len(grid[0])

    q = [(0, 0, 0)]
    min_cost = {(0,0): 0}

    while q:
        cost, r, c = q.pop(0)

        if (r, c) == (num_rows - 1, num_cols - 1):
            return cost

        for d, (dr, dc) in enumerate(dirs):
            new_r, new_c = r + dr, c + dc
            new_cost = cost + (0 if d == grid[r][c]-1 else 1)
            if ((new_r < 0 or new_c < 0) or 
                (new_r == num_rows or new_c == num_cols) or 
                (new_cost >= min_cost.get((new_r, new_c), float("inf")))):
                continue
            
            min_cost[(new_r,new_c)] = new_cost
            if d == grid[r][c]-1:
                q.insert(0, (new_cost, new_r, new_c))
            else:
                q.append((new_cost, new_r, new_c))

if __name__ == '__main__':

    case1 = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    case2 = [[1,1,3],[3,2,2],[1,1,4]]
    case3 = [[1,2],[4,3]]

    print(minCost(case1))
    print(minCost(case2))
    print(minCost(case3))
