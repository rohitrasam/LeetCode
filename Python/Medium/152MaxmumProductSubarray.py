# https://leetcode.com/problems/maximum-product-subarray/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def maxProduct(nums: List[int]) -> int:
    res = max(nums)

    curMax = 1
    curMin = 1

    for num in nums:
        if num == 0:
            curMax = 1
            curMin = 1
            continue

        temp = curMax * num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(temp, num * curMin, num)

        res = max(res, curMax, curMin)
    
    return res

if __name__ == '__main__':

    case = [2,3,-2,4]
    print(maxProduct(case))

    case = [-2,0,-1]
    print(maxProduct(case))

    case = [-1,2,3,4,-2,2,4,0,1]
    print(maxProduct(case))

