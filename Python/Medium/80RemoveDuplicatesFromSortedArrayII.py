# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=problem-list-v2&envId=two-pointers



from typing import List


def removeDuplicates(nums: List[int]) -> int:
    
    """ My Solution TC: O(n^2)"""
    # counter = 1
    # l = 0
    # r = len(nums) - 1

    # while l < r:
        
    #     if nums[l] == nums[l+1]:
    #         counter += 1
    #     else:
    #         counter = 1
    #     if counter > 2:
    #         elem = nums.pop(l)
    #         nums.insert(r+1, elem)
    #         r -= 1
    #         counter -= 1
    #     else:
    #         l += 1
    
    # return r+1

    """ TC: O(n) """

    l, r = 0, 0

    while r < len(nums):
        count = 1

        while r + 1 < len(nums) and nums[r] == nums[r+1]:
            r += 1
            count += 1
        
        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1

        r += 1
        
    return l


if __name__ == '__main__':

    case = [1,1,1,2,2,3]
    print(removeDuplicates(case))
    case = [0,0,1,1,1,1,2,3,3]
    print(removeDuplicates(case))