# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/description/?envType=problem-list-v2&envId=sliding-window


from typing import List


def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
    longest = 0 
    current = 0 
    for i in range(len(nums)): 
        if nums[i] > threshold: 
            current = 0 
        elif current == 0 and nums[i] % 2 == 0: 
            current = 1 
        elif current > 0 and nums[i] % 2 != nums[i - 1] % 2: 
            current += 1 
        else: 
            current = 1 if nums[i] % 2 == 0 else 0 
        longest = max(longest, current) 
    return longest 

if __name__ == '__main__':

    case = [8, 4], 6
    print(longestAlternatingSubarray(*case))
    case = [10, 8], 4
    print(longestAlternatingSubarray(*case))
    case = [3,2,5,4], 5
    print(longestAlternatingSubarray(*case))
    case = [1,2], 2
    print(longestAlternatingSubarray(*case))
    case = [2,3,4,5], 4
    print(longestAlternatingSubarray(*case))
    case = [2,3,4,5,3,2,5,4], 4
    print(longestAlternatingSubarray(*case))
