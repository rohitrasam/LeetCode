# https://leetcode.com/problems/partition-equal-subset-sum/description/

from typing import List


def canPartition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False
    
    dp = set()
    dp.add(0)

    target = sum(nums) // 2

    for i in range(len(nums)-1, -1, -1):
        nextDP = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP
    
    return True if target in dp else False



if __name__ == '__main__':

    case = [1,5,11,5]
    print(canPartition(case))
    case = [1,2,3,5]
    print(canPartition(case))
