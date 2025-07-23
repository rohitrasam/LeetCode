from typing import List

def maxSubarray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    curSum = 0
    maxSum = nums[0]
    for num in nums:
        curSum = max(curSum, 0)
        curSum += num
        maxSum = max(maxSum, curSum)
    
    return maxSum



if __name__ == '__main__':

    case1 = [-2,1,-3,4,-1,2,1,-5,4]
    case2 = [1]
    case4 = [1,2]
    case3 = [5,4,-1,7,8]

    print(maxSubarray(case1))
    print(maxSubarray(case2))
    print(maxSubarray(case3))
    print(maxSubarray(case4))