# https://leetcode.com/problems/house-robber-ii/description/?envType=problem-list-v2&envId=dynamic-programming

from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) <= 3:
        return max(nums)
    
    return max(helper(nums[1:]), helper(nums[:-1]))

def helper(nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2



if __name__ == '__main__':

    case = [2,3,2]
    print(rob(case))
    case = [1,2,3,1]
    print(rob(case))
    case = [1,2,3]
    print(rob(case))
    case = [2,3]
    print(rob(case))
    case = [2]
    print(rob(case))
    case = [2,7,9,3,1,4]
    print(rob(case))
    case = [2,7,9,3,1]
    print(rob(case))