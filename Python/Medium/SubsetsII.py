# https://leetcode.com/problems/combination-sum-ii/?envType=problem-list-v2&envId=backtracking

from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    subset = []
    def backtrack(i: int) -> None:
        if i >= len(nums):
            res.append(subset[:])
            return
        
        subset.append(nums[i])
        backtrack(i+1)
        subset.pop()

        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        
        backtrack(i+1)
    
    backtrack(0)
    return res



if __name__ == '__main__':

    case = [1,2,2]
    print(subsetsWithDup(case))
    case = [0]
    print(subsetsWithDup(case))
    case = [1,2,3,2]
    print(subsetsWithDup(case))