# https://leetcode.com/problems/find-a-peak-element-ii/description/


from typing import List


def findPeakGrid(mat: List[List[int]]) -> List[int]:
    
    # rows, cols = len(mat), len(mat[0])

    # for row in range(rows):
    #     for col in range(cols):

    #         l_elem = -1 if col == 0 else mat[row][col-1]
    #         r_elem = -1 if col == cols-1 else mat[row][col+1]
    #         t_elem = -1 if row == 0 else mat[row-1][col]
    #         b_elem = -1 if row == rows-1 else mat[row+1][col]

    #         if l_elem < mat[row][col] and r_elem < mat[row][col] and t_elem < mat[row][col] and b_elem < mat[row][col]:
    #             return [row, col]

    # return -1

    rows, cols = len(mat), len(mat[0])
    start, end = 0, len(mat[0]) - 1

    while start <= end:
        max_row = 0
        mid_col = (start + end) // 2

        for row in range(rows):
            max_row = row if mat[row][mid_col] >= mat[max_row][mid_col] else max_row
        
        leftIsBig = mid_col - 1 >= start and mat[max_row][mid_col-1] > mat[max_row][mid_col]
        rightIsBig =  mid_col + 1 <= end and mat[max_row][mid_col+1] > mat[max_row][mid_col]

        if not leftIsBig and not rightIsBig:
            return [max_row, mid_col]
        elif rightIsBig:
            start = mid_col + 1
        else:
            end = mid_col - 1
    
    return []

if __name__ == '__main__':

    case1 = [
                [1,4],
                [3,2]
            ]
    case2 = [
                [10,20,15],
                [21,30,14],
                [7,16,32]
            ]
    case3 = [
                [70,50,40,30,20],
                [100,1,2,3,4]
            ]
    case4 = [
                [4, 2, 5, 1, 4, 5],
                [2, 9, 3, 2, 3, 2],
                [1, 7, 6, 0, 1, 3],
                [3, 6, 2, 3, 7, 2]
            ]

    print(findPeakGrid(case1))
    print(findPeakGrid(case2))
    print(findPeakGrid(case3))
    print(findPeakGrid(case4))