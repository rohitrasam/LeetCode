# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    # nums.sort()

    # left, right = 0, len(nums) -1
    # ops = 0

    # while left < right:
    #     total = nums[left] + nums[right]
    #     if total == k:
    #         ops += 1
    #         left += 1
    #         right -= 1
    #     elif total < k:
    #         left += 1
    #     else: 
    #         right -= 1

    # return ops

    hashmap = {}
    ops = 0
    for num in nums:
        diff = k - num
        if hashmap.get(diff):
            ops += 1
            hashmap[diff] -= 1
        elif hashmap.get(num):
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    
    return ops

if __name__ == '__main__':
    case1 = [1,2,3,4], 5
    case2 = [3,1,3,4,3], 6
    case3 = [4, 2, 6, 1, 9, 10, 3], 4

    print(maxOperations(*case1))
    print(maxOperations(*case2))
    print(maxOperations(*case3))
