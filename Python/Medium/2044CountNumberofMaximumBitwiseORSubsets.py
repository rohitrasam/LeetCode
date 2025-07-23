# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def countMaxOrSubsets(nums: List[int]) -> int:
    
    maxOr = 0
    for num in nums:
        maxOr |= num

    res = 0

    def dfs(idx: int, currOr: int) -> None:
        if idx == len(nums):
            
            nonlocal maxOr, res
            if currOr == maxOr:
                res += 1
            return
        
        dfs(idx + 1, currOr | nums[idx])

        dfs(idx + 1, currOr)

    dfs(0, 0)
    return res

if __name__ == '__main__':

    # case = [3,1]
    # print(countMaxOrSubsets(case))
    case = [2,2,2]
    print(countMaxOrSubsets(case))
    case = [3,2,1,5]
    print(countMaxOrSubsets(case))


