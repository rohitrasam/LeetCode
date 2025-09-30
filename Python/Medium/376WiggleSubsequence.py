# https://leetcode.com/problems/wiggle-subsequence/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def wiggleMaxLength(nums: List[int]) -> int:

    up = 1
    down = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            up = down + 1
        elif nums[i] < nums[i-1]:
            down = up + 1
        
    return max(up, down)


if __name__ == '__main__':

    case = [1,7,4,9,2,5]
    print(wiggleMaxLength(case))
    case = [1,17,5,10,13,15,10,5,16,8]
    print(wiggleMaxLength(case))
    case = [1,2,3,4,5,6,7,8,9]
    print(wiggleMaxLength(case))