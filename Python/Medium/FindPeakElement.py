# https://leetcode.com/problems/find-peak-element/


from typing import List


def findPeakElement(nums: List[int]) -> int:
    # n = len(nums)

    # for idx in range(len(nums)):
    #     if (idx > 0 and  nums[idx-1] < nums[idx]) and (idx < n-1 and nums[idx] > nums[idx+1]):
    #         return idx
    #     else:
    #         if (idx == 0 and nums[idx] > nums[idx+1]) or (idx == n -1 and nums[idx] > nums[idx-1]):
    #             return idx

    n = len(nums)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        l_elem = float('-inf') if m == 0 else nums[m-1]
        r_elem = float('-inf') if m == n-1 else nums[m+1]

        if l_elem < nums[m] and r_elem < nums[m]:
            return m
        elif l_elem > nums[m]:
            r = m - 1
        elif r_elem > nums[m]:
            l = m + 1


if __name__ == '__main__':

    case1 = [1,2,3,1]
    case2 = [1,2,1,3,5,6,4]
    case3 = [1,2]

    print(findPeakElement(case1))
    print(findPeakElement(case2))
    print(findPeakElement(case3))
