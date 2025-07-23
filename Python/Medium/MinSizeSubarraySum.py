# https://leetcode.com/problems/minimum-size-subarray-sum/description/


from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    # n = len(nums)
    # prefix = []
    # total = 0
    # for num in nums:
    #     total += num
    #     prefix.append(total)
        
    # min_size = float('inf')
    # l = 0
    # for r in range(n):
    #     while (l > 0 and prefix[r] - prefix[l-1] >= target) or (l == 0 and prefix[r] >= target):
    #         min_size = min(min_size, r - l + 1)
    #         l += 1

    # return 0 if min_size == float('inf') else min_size

    n = len(nums)
    total = 0
    min_size = float('inf')
    l = 0
    for r in range(n):
        total += nums[r]
        while total >= target:
            min_size = min(min_size, r - l + 1)
            total -= nums[l]
            l += 1
    
    return 0 if min_size == float('inf') else min_size


if __name__ == '__main__':
    case1 = 7, [2,3,1,2,4,3]
    case2 = 4, [1,4,4]
    case3 = 11, [1,1,1,1,1,1,1,1]

    print(minSubArrayLen(*case1))    
    print(minSubArrayLen(*case2))
    print(minSubArrayLen(*case3))    
