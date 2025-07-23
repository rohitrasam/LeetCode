# https://leetcode.com/problems/count-special-quadruplets/description/?envType=problem-list-v2&envId=hash-table

from typing import List


def countQuadruplets(nums: List[int]) -> int:
    pair_sum_counts = {}  # sum -> number of (a,b) pairs with a<b<current_c
    count = 0
    n = len(nums)

    for c in range(n):
        # 1. For each d > c, check how many pairs (a,b) sum to nums[d] - nums[c]
        for d in range(c+1, n):
            needed = nums[d] - nums[c]
            if needed in pair_sum_counts:
                count += pair_sum_counts[needed]

        # 2. After checking d, add all pairs (i, c) for i < c to the map
        for i in range(c):
            s = nums[i] + nums[c]
            pair_sum_counts[s] = pair_sum_counts.get(s, 0) + 1

    return count


if __name__ == '__main__':
    case = [1,2,3,6]
    print(countQuadruplets(case))
    case = [3,3,6,4,5]
    print(countQuadruplets(case))
    case = [1,1,1,3,5]
    print(countQuadruplets(case))
    case = [4,6,1,11,18,21] 
    print(countQuadruplets(case))