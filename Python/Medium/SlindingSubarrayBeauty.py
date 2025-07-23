# https://leetcode.com/problems/sliding-subarray-beauty/?envType=problem-list-v2&envId=sliding-window


from typing import List


def getSubarrayBeauty(nums: List[int], k: int, x: int) -> List[int]:
    pass


if __name__ == '__main__':

    case = [1,-1,-3,-2,3], 3, 2
    print(getSubarrayBeauty(*case))
    case = [-1,-2,-3,-4,-5], 2, 2
    print(getSubarrayBeauty(*case))
    case = [-3,1,2,-3,0,-3], 2, 1
    print(getSubarrayBeauty(*case))
    case = [-3,1,2,-3,0,-3], 2, 2
    print(getSubarrayBeauty(*case))
    case = [-3,1,2,-3,0,-3], 4, 2
    print(getSubarrayBeauty(*case))
