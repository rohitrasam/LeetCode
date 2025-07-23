# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    
    def binSearch(leftBias: bool) -> int:
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
    
    pos = [binSearch(True), binSearch(False)]
    return pos
        

if __name__ == '__main__':

    case1 = [5,7,7,8,8,10], 8
    case2 = [5,7,7,8,8,10], 6
    case3 = [], 0

    print(searchRange(*case1))
    print(searchRange(*case2))
    print(searchRange(*case3))