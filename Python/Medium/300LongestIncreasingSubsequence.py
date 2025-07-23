# https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def lengthOfLIS(nums: List[int]) -> int:

    """ Neetcode Solution """
    # LIS = [1] * len(nums)

    # for i in range(len(nums) - 1, -1, -1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] < nums[j]:
    #             LIS[i] = max(LIS[i], 1 + LIS[j])
        
    # return max(LIS)

    """ My solution """
    res = 1

    def dfs(i: int, cur_len: int) -> None:
        nonlocal res

        if i >= len(nums):
            res = max(res, cur_len)
            return
        
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                dfs(j, cur_len+1)
    
    dfs(0, 1)
    return res


if __name__ == '__main__':

    case = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS(case))
    case = [0,1,0,3,2,3]
    print(lengthOfLIS(case))
    case = [7,7,7,7,7,7,7]
    print(lengthOfLIS(case))
