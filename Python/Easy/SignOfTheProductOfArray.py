# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

from typing import List


def arraySign(nums: List[int]) -> int:
    sign = 0

    for num in nums:
        if num < 0:
            sign = not sign
        elif num == 0:
            return 0
    
    return -1 if sign else 1


if __name__ == '__main__':
    
    case1 = [-1,-2,-3,-4,3,2,1]
    case2 = [1,5,0,2,-3]
    case3 = [-1,1,-1,1,-1]

    print(arraySign(case1))
    print(arraySign(case2))
    print(arraySign(case3))