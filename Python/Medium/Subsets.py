# https://leetcode.com/problems/subsets/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    
    res = []

    subset = []

    def dfs(i: int) -> None:
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)
    
    dfs(0)
    return res


if __name__ == '__main__':

    case = [1,2,3]
    print(subsets(case))
    case = [0]
    print(subsets(case))
