from typing import List
from functools import reduce

def productExceptSelf(nums: List[int]) -> List[int]:
    out = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        out[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] *= postfix
        postfix *= nums[i]

    return out

if __name__ == '__main__':
    case1 = [1,2,3,4]
    case2 = [-1,1,0,-3,3]
    print(productExceptSelf(case1))
    print(productExceptSelf(case2))