from typing import List


def waysToSplitArray(nums: List[int]) -> int:
    prefixSums = [0] * len(nums)
    prefixSum = 0
    splits = 0

    for idx, num in enumerate(nums):
        prefixSum += num
        prefixSums[idx] = prefixSum
    
    for i in range(len(nums) -1):
        left = prefixSums[i]
        right = prefixSums[-1] - prefixSums[i]
        if left >= right:
            splits += 1

    return splits

if __name__ == '__main__':
    case1 = [10,4,-8,7]
    case2 = [2,3,1,0]
    case3 = [9,1,6,12,-2,-12,3,10]

    print(waysToSplitArray(case1))
    print(waysToSplitArray(case2))
    print(waysToSplitArray(case3))
