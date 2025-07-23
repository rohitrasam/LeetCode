# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/


from typing import List


def canPartitionKSubsets(nums: List[int], k: int) -> bool:

    if sum(nums) % k:
        return False
    
    nums.sort(reverse=True)
    target = sum(nums) / k

    used = [False] * len(nums)

    def backTrack(i: int, k: int, subsetSum: int):
        if k == 0:
            return True
        if subsetSum == target:
            return backTrack(0, k - 1, 0)
        
        for j in range(i, len(nums)):
            if used[j] or subsetSum + nums[j] > target:
                continue
            used[j] = True
            if backTrack(j + 1, k, subsetSum + nums[j]):
                return True
            
            used[j] = False

        return False
    
    return backTrack(0, k, 0)



if __name__ == '__main__':

    case = [4,3,2,3,5,2,1], 4
    print(canPartitionKSubsets(*case))
    case = [1,2,3,4], 3
    print(canPartitionKSubsets(*case))