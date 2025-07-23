# https://leetcode.com/problems/3sum-closest/description/

from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    # nums.sort()
    # res = 0
    # closest = {}

    # for idx in range(len(nums)-2):
    #     low = idx + 1
    #     high = len(nums) - 1
    #     while low < high:
    #         res = sum((nums[idx], nums[low], nums[high]))
    #         closest.setdefault(abs(target-res), res)
    #         if res < target:
    #             low += 1
    #         else:
    #             high -= 1

    # return closest[min(closest)]

    nums.sort()
    res = 0
    closest = 10**5

    for idx in range(len(nums)-2):
        low = idx + 1
        high = len(nums) - 1
        while low < high:
            res = nums[idx] + nums[low] + nums[high]
            if abs(target - res) < abs(target - closest):
                closest = res
            elif res < target:
                low += 1
            else:
                high -= 1

    return closest

if __name__ == '__main__':

    case1 = [-1,2,1,-4], 1
    case2 = [0,0,0], 1
    case3 = [-2, 1, -8, 6, 0, 3], 4

    print(threeSumClosest(*case1))
    print(threeSumClosest(*case2))
    print(threeSumClosest(*case3))