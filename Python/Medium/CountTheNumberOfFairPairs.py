# https://leetcode.com/problems/count-the-number-of-fair-pairs/

# TODO
from typing import List


def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    
    pairs =0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if lower <= nums[i] + nums[j] <= upper:
                pairs += 1

    return pairs


if __name__ == '__main__':

    case = [0,1,7,4,4,5], 3, 6
    print(countFairPairs(*case))
    case = [1,7,9,2,5], 11, 11
    print(countFairPairs(*case))
