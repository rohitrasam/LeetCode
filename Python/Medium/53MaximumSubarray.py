# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


def maxSubArray(nums: List[int]) -> int:
    maxSum = float("-inf")
    curSum = 0

    for num in nums:
        curSum += num
        maxSum = max(curSum, maxSum)
        curSum = max(0, curSum)    
    return maxSum
        


if __name__ == '__main__':

    case = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(case))
    case = [1]
    print(maxSubArray(case))
    case = [5,4,-1,7,8]
    print(maxSubArray(case))
