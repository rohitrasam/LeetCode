# https://leetcode.com/problems/maximum-erasure-value/description/?envType=problem-list-v2&envId=sliding-window


from typing import List


def maximumUniqueSubarray(nums: List[int]) -> int:
    # max_score = 0
    # l = 0
    # dupes = set()
    # for r in range(len(nums)):
    #     if nums[r] in dupes:
    #         max_score = max(max_score, sum(dupes))
    #         while nums[r] in dupes:
    #             dupes.remove(nums[l])
    #             l += 1
            
    #     dupes.add(nums[r])

    # return max(max_score, sum(dupes))

    max_score = 0
    l = 0
    dupes = set()
    total = 0
    for r in range(len(nums)):
        total += nums[r]
        if nums[r] in dupes:
            max_score = max(max_score, total-nums[r])
            while nums[r] in dupes:
                dupes.remove(nums[l])
                total -= nums[l]
                l += 1
            
        dupes.add(nums[r])

    return max(max_score, sum(dupes))



if __name__ == '__main__':
    case = [4,2,4,5,6]
    print(maximumUniqueSubarray(case))
    case = [5,2,1,2,5,2,1,2,5]
    print(maximumUniqueSubarray(case))
