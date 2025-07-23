# https://leetcode.com/problems/count-number-of-bad-pairs/description/

from typing import List


def countBadPairs(nums: List[int]) -> int:
    n = len(nums)
    
    pairs = {}
    g_pairs = 0
    for i in range(n):
        con = nums[i] - i
        if con in pairs:
            g_pairs += pairs[con]
        pairs[con] = pairs.get(con, 0) + 1

    return (n * (n-1) // 2) - g_pairs

if __name__ == '__main__':

    case = [4,1,3,3]
    print(countBadPairs(case))

    case = [1,2,3,4,5]
    print(countBadPairs(case))