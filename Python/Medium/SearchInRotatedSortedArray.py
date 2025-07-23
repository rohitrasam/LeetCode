# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if target == nums[m]:
            return m
        
        # left sorted array
        if nums[l] <= nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        # right sorted array
        else:
            if target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    
    return -1

        

if __name__ == '__main__':

    case1 = [4,5,6,7,0,1,2],0
    case2 = [4,5,6,7,0,1,2],3
    case3 = [1],0
    case4 = [4,5,6,7,0,1,2],2

    print(search(*case1))
    print(search(*case2))
    print(search(*case3))
    print(search(*case4))