# https://leetcode.com/problems/arithmetic-slices/?envType=problem-list-v2&envId=sliding-window


from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:
    # n = len(nums)
    # dp = [0] * n

    # for i in range(2, n):
    #     if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
    #         dp[i] = 1 + dp[i-1]
    
    # return sum(dp)

    # n = len(nums)
    # dp = 0
    # res = 0

    # for i in range(2, n):
    #     if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
    #         dp += 1
    #         res += dp
    #     else:
    #         dp = 0

    # return res

    n = len(nums)
    count = 0
    res = 0

    for i in range(2, n):
        if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
            count += 1
        else:
            res += (count * (count + 1) / 2)
            count = 0

    return int(res + (count * (count + 1) / 2))



if __name__ == '__main__':
    case = [1,2,3,4]
    print(numberOfArithmeticSlices(case))    
    case = [1]
    print(numberOfArithmeticSlices(case))