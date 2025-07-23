# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/?envType=problem-list-v2&envId=sliding-window


from typing import List


def resultsArray(nums: List[int], k: int) -> List[int]:
    if k == 1:
        return nums
    
    n = len(nums)
    res = [-1] * (n - k + 1)
    cons_count = 1

    for i in range(1, n):
        if nums[i] == 1 + nums[i-1]:
            cons_count += 1
        else:
            cons_count = 1

        if cons_count >= k:
            res[i - k + 1] = nums[i]
    
    return res

if __name__ == '__main__':

    case = [1,2,3,4,3,2,5], 3
    print(resultsArray(*case))
    case = [2,2,2,2,2], 4
    print(resultsArray(*case))
    case = [3,2,3,2,3,2], 2
    print(resultsArray(*case))