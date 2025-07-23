# https://leetcode.com/problems/target-sum/description/?envType=problem-list-v2&envId=dynamic-programming


from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple


def findTargetSumWays(nums: List[int], target: int) -> int:
    """Backtracking:"""

    # def bt(i: int, total: int) -> int:
    #     if i == len(nums):
    #         return total == target

    #     return bt(i + 1, total + nums[i]) + bt(i + 1, total - nums[i])

    # return bt(0, 0)

    """DP: Top-Down"""
    dp: Dict[Tuple[int, int], int] = {}

    def bt(i: int, total: int) -> int:
        if (i, total) in dp:
            return dp[(i, total)]

        if i == len(nums):
            return total == target

        dp[(i, total)] = bt(i + 1, total - nums[i]) + bt(i + 1, total + nums[i])

        return dp[(i, total)]

    return bt(0, 0)

    """DP: Bottom-Up"""
    # dp: List[DefaultDict[int, int]] = [defaultdict(int) for _ in range(len(nums) + 1)]
    # dp[0][0] = 1

    # for i in range(len(nums)):
    #     for cur_sum, count in dp[i].items():
    #         dp[i+1][cur_sum + nums[i]] += count
    #         dp[i+1][cur_sum - nums[i]] += count

    # return dp[len(nums)][target]

    """DP: Bottom-Up (Space Optimized)"""
    # dp: DefaultDict[int, int] = defaultdict(int)
    # dp[0]= 1

    # for i in range(len(nums)):
    #     next_dp: DefaultDict[int] = defaultdict(int)
    #     for cur_sum, count in dp.items():
    #         next_dp[cur_sum + nums[i]] += count
    #         next_dp[cur_sum - nums[i]] += count
    #     dp = next_dp

    # return dp[target]


if __name__ == "__main__":
    case = [1, 1, 1, 1, 1], 3
    print(findTargetSumWays(*case))
    case = [1, 1, 1, 1, 1, 1], 2
    print(findTargetSumWays(*case))
    case = [1, 1, 1, 1, 1, 1], 3
    print(findTargetSumWays(*case))
    case = [1], 1
    print(findTargetSumWays(*case))
