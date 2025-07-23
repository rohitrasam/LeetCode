# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=daily-question&envId=2025-01-16

from typing import List


def xorAllNums(nums1: List[int], nums2: List[int]) -> int:

    n1, n2 = len(nums1), len(nums2)
    xor = {}

    for num1 in nums1:
        xor[num1] = xor.get(num1, 0) + n2
    
    for num2 in nums2:
        xor[num2] = xor.get(num2, 0) + n1
    
    ans = 0
    for x in xor:
        if xor[x] % 2:
            ans ^= x

    return ans      


if __name__ == '__main__':

    case1 = [2,1,3], [10,2,5,0]
    case2 = [1,2], [3,4]

    print(xorAllNums(*case1))
    print(xorAllNums(*case2))