from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bot = 0, ROWS-1

    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top += 1
        elif target < matrix[row][0]:
            bot -= 1
        else:
            break
    
    if not(top <= bot):
        return False
    
    left, right = 0, COLS-1
    while left <= right:
        mid = (left + right) // 2
        if target < matrix[row][mid]:
            right = mid - 1
        elif target > matrix[row][mid]:
            left = mid + 1
        else:
            return True
    
    return False

if __name__ == '__main__':

    case1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
    case2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13

    print(searchMatrix(*case1))
    print(searchMatrix(*case2))