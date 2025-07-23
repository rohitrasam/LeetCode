# https://leetcode.com/problems/map-of-highest-peak/description/?envType=daily-question&envId=2025-01-22


from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:

    dirs = ((-1, 0), (0, 1), (0, -1), (1, 0))
    rows, cols = len(isWater), len(isWater[0])
    height = [[-1] * cols for _ in range(rows)]
    q = []

    for row in range(rows): 
        for col in range(cols):
            if isWater[row][col]:
                q.append((row, col))
                height[row][col] = 0
    
    next_layer = 1

    def valid_cell(row: int, col: int):
        return 0 <= new_row < rows and  0 <= new_col < cols

    while q:
        q_size = len(q)
        for _ in range(q_size):
            cur_row, cur_col = q.pop(0)
            for dr, dc in dirs:
                new_row, new_col = cur_row + dr, cur_col + dc
                if valid_cell(new_row, new_col) and height[new_row][new_col] == -1:
                    height[new_row][new_col] = next_layer
                    q.append((new_row, new_col))
                
        next_layer += 1

    return height

if __name__ == '__main__':
    case1 = [[0,1],[0,0]]
    case2 = [[0,0,1],[1,0,0],[0,0,0]]

    # print(highestPeak(case1))
    print(highestPeak(case2))
