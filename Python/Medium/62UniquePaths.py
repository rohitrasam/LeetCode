# https://leetcode.com/problems/unique-paths/description/?envType=problem-list-v2&envId=dynamic-programming

def uniquePaths(m: int, n: int) -> int:

    """ DFS: Recurrsion """
    # def dfs(row: int, col: int):

    #     if row >= m or col >= n:
    #         return 0
    #     if row == m-1 and col == n-1:
    #         return 1
        
    #     return dfs(row + 1, col) + dfs(row, col + 1)

    # return dfs(0, 1) + dfs(1, 0)

    """ DP """

    row = [1] * n   # the bottom row

    for i in range(m-1):    # going through the other rows except the last one
        newRow = [1]  * n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    
    return row[0]

if __name__ == '__main__':

    case = 3, 7
    print(uniquePaths(*case))
    case = 3, 2
    print(uniquePaths(*case))
