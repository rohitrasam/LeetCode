# https://leetcode.com/problems/maximum-good-subarray-sum/description/

from collections import defaultdict
from typing import List

large = lambda: 10**14

def maxSubarraySum(nums: List[int], k: int) -> int:
    # prefix_left = {}
    prefix_left = defaultdict(large)
    res = -large()
    cur = 0

    for x in nums:
        # prefix_left.setdefault(x, min(prefix_left.get(x, 10**14), cur))
        prefix_left[x] = min(prefix_left[x], cur)
        cur += x

        if x - k in prefix_left:
            res = max(res, cur - prefix_left[x-k])
        if x + k in prefix_left:
            res = max(res, cur - prefix_left[x+k])
    
    return res if res != -large() else 0

if __name__ == '__main__':

    # case1 = [1,2,3,4,5,6], 1
    # case2 = [-1,3,2,4,5], 3
    # case3 = [-1,-2,-3,-4], 2
    case4 = [2, -1, 6, 0, -2, -3, 4], 4

    # print(maxSubarraySum(*case1))
    # print(maxSubarraySum(*case2))
    # print(maxSubarraySum(*case3))
    print(maxSubarraySum(*case4))