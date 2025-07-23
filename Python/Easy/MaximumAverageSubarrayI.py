# https://leetcode.com/problems/maximum-average-subarray-i/?envType=problem-list-v2&envId=sliding-window


from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    # l = 0
    # total = sum(nums[l:k])
    # max_avg = total / k
    # for r in range(k, len(nums)):
    #     total += nums[r] - nums[l]
    #     l += 1
    #     max_avg = max(max_avg, total / k)
    
    # return max_avg

    total = sum(nums[:k])
    max_avg = total / k
    for i in range(1, len(nums)-k+1):
        total += nums[i+k-1] - nums[i-1]
        max_avg = max(max_avg, total / k)
    
    return max_avg


if __name__ == '__main__':
    case = [1,12,-5,-6,50,3], 4
    print(findMaxAverage(*case))
    case = [5], 1
    print(findMaxAverage(*case))
