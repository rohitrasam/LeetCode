# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/?envType=problem-list-v2&envId=sliding-window

from typing import Dict, List


def countCompleteSubarrays(nums: List[int]) -> int:
    
    dist: int = len(set(nums))
    cnt: Dict[int, int] = {}
    res: int = 0
    n: int = len(nums)
    r: int = 0

    for l in range(n):
        if l > 0:
            rem = nums[l-1]
            cnt[rem] -= 1
            if cnt[rem] == 0:
                cnt.pop(rem)
        
        while r < n and len(cnt) < dist:
            cnt[nums[r]] = cnt.get(nums[r], 0) + 1
            r += 1
        
        if len(cnt) == dist:
            res += n - r + 1
    
    return res


if __name__ == '__main__':

    case = [1,3,1,2,2, 3]
    print(countCompleteSubarrays(case))
    case = [1,3,1,2,2,4,3]
    print(countCompleteSubarrays(case))
    case = [5,5,5,5]
    print(countCompleteSubarrays(case))