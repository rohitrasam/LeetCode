from typing import List


# def maxWidthRamp(nums: List[int]) -> int:
#     indices = []
#     for i in range(len(nums)):
#         if not indices or nums[indices[-1]] > nums[i]:
#             indices.append(i)

        
#     maxWidth = 0
#     for j in range(len(nums)-1, -1, -1):
#         while indices and nums[indices[-1]] <= nums[j]:
#             maxWidth = max(maxWidth, j - indices.pop())
        
#     return maxWidth
def maxWidthRamp(nums: List[int]) -> int:
    n = len(nums)
    rightMax = [None] * n
    rightMax[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
        rightMax[i] = max(rightMax[i+1], nums[i])

    left = right = 0
    maxWidth = 0

    while right < n:
        while left < right and nums[left] > rightMax[right]:
            left += 1
        maxWidth = max(maxWidth, right - left)
        right += 1

    return maxWidth


if __name__ == '__main__':

    case1 = [6,0,8,2,1,5]
    case2 = [9,8,1,0,1,9,4,0,4,1]

    print(maxWidthRamp(case1))
    print(maxWidthRamp(case2))