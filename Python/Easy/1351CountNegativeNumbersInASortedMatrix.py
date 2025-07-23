# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/?envType=problem-list-v2&envId=binary-search


from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    """ Brute Force """

    # count = 0
    # for x in range(len(grid)):
    #     for y in range(len(grid[0])):
    #         if grid[x][y] < 0:
    #             count += 1
    
    # return count

    """ Optimized Solution """
    rows = len(grid)

    counter = 0
    col = len(grid[0]) - 1
    row = 0

    while row < rows and col >= 0:
        if(grid[row][col] < 0):
            counter += rows - row
            col -= 1
        else:
            row += 1
    
    return counter

if __name__ == '__main__':

    case = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(countNegatives(case))
    case = [[3,2],[1,0]]
    print(countNegatives(case))
    case = [[5,1,0],[-5,-5,-5]]
    print(countNegatives(case))
    