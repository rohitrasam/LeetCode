# https://leetcode.com/problems/find-closest-number-to-zero/description/

from typing import List


def findClosestNumber(nums: List[int]) -> int:
    # l, r = 0, len(nums) - 1

    # while l < r:
    #     if abs(nums[l]) < abs(nums[r]):
    #         r -= 1
    #     elif abs(nums[r]) < abs(nums[l]):
    #         l += 1
    #     else:
    #         if nums[l] < nums[r]:
    #             l += 1
    #         else:
    #             r -= 1

    # return nums[r]

    dist = float('inf')
    num = float('-inf')

    for i in range(len(nums)):
        curr_dist = abs(nums[i])

        if curr_dist < dist:
            dist = curr_dist
            num = nums[i]
        elif curr_dist == dist:
            num = max(num, nums[i])

    return num
            


if __name__ == '__main__':

    case = [-4,-2,1,4,8]
    print(findClosestNumber(case))
    case = [-4,-2,-1,2,4,8]
    print(findClosestNumber(case))
    case = [4,2,2,4,8]
    print(findClosestNumber(case))
    case = [-4,-2,-2,-4,-8]
    print(findClosestNumber(case))
    case = [2,-1,1]
    print(findClosestNumber(case))