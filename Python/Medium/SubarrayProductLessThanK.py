# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=sliding-window


from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    
    count = 0
    l = 0
    prod = 1
    for r in range(len(nums)):
        prod *= nums[r]
        while prod >= k:
            prod //= nums[l]
            l += 1
        count += r - l + 1
    
    return count


if __name__ == '__main__':

    case = [10,5,2,6], 100
    print(numSubarrayProductLessThanK(*case))
    case = [1,2,3], 0
    print(numSubarrayProductLessThanK(*case))
