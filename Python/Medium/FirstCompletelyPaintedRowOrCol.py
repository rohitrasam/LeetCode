# https://leetcode.com/problems/first-completely-painted-row-or-column/description/?envType=daily-question&envId=2025-01-20

from typing import List

""" Brute force: Counting rows and cols"""
# def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:

#     painted = {}
#     rows, cols = len(mat), len(mat[0])

#     row_count = [0] * rows
#     col_count = [0] * cols
    
#     for row in range(rows):
#         for col in range(cols):
#             painted[mat[row][col]] = (row, col)
        
#     for i, num in enumerate(arr):
#         row, col = painted[num]
#         row_count[row] += 1
#         col_count[col] += 1
    
#         if row_count[row] == cols or col_count[col] == rows:
#             return i
    
#     return -1

""" Reverse Mapping """
def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:

    painted = {}
    rows, cols = len(mat), len(mat[0])

    for idx in range(len(arr)):
        painted[arr[idx]] = idx

    result = float('inf')

    for row in range(rows):
        last_elem_idx = float('-inf')
        for col in range(cols):
            index_val = painted[mat[row][col]]
            last_elem_idx = max(last_elem_idx, index_val)
        
        result = min(result, last_elem_idx)

    for col in range(cols):
        last_elem_idx = float('-inf')
        for row in range(rows):
            index_val = painted[mat[row][col]]
            last_elem_idx = max(last_elem_idx, index_val)
        
        result = min(result, last_elem_idx)

    return result

if __name__ == '__main__':

    case1 = [1,3,4,2], [[1,4],
                        [2,3]]
    case2 = [2,8,7,4,1,3,5,6,9], [[3,2,5],
                                  [1,4,6],
                                  [8,7,9]]
    
    print(firstCompleteIndex(*case1))
    print(firstCompleteIndex(*case2))