# https://leetcode.com/problems/find-missing-and-repeated-values/description/

from typing import Dict, List


def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    h_table: Dict[int, int] = {}
    
    for row in grid:
        for col in row:
            h_table[col] = 1 + h_table.get(col, 0)
    
    n = len(grid)
    for i in range(1, (n*n)+1):
        if i not in h_table:
            missing = i
        elif h_table[i] == 2:
            repeat = i
    
    return repeat, missing

    


if __name__ == "__main__":
    case = [[1, 3], [2, 2]]
    print(findMissingAndRepeatedValues(case))
    case = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    print(findMissingAndRepeatedValues(case))
