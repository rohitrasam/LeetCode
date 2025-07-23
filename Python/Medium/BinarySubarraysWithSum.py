# https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:

    # start, pre_zeros, cur_sum, total = 0, 0, 0, 0
    
    # for end, num in enumerate(nums):
    #     cur_sum += num

    #     while start < end and (cur_sum > goal or nums[start] == 0):
    #         if nums[start] == 1:
    #             pre_zeros = 0
    #         else:
    #             pre_zeros += 1
            
    #         cur_sum -= nums[start]
    #         start += 1
        
    #     if cur_sum == goal:
    #         total += 1 + pre_zeros
        
    # return total

    count = 0
    total = 0
    pre_sum = {}
    for num in nums:
        total += num
        if total == goal:
            count += 1
        
        if total - goal in pre_sum:
            count += pre_sum[total - goal]
        
        pre_sum[total] = 1 + pre_sum.get(total, 0)
    
    return count



if __name__ == '__main__':

    case = [1,0,1,0,1], 2
    print(numSubarraysWithSum(*case))
    case = [1,0,1,1,1,0,0,1], 3
    print(numSubarraysWithSum(*case))
    case = [0,0,0,0,0], 0
    print(numSubarraysWithSum(*case))
