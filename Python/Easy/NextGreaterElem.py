from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    numsIndx = {n:i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []

    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and cur > stack[-1]:
            val = stack.pop()
            idx = numsIndx[val]
            res[idx] = cur
        if cur in numsIndx:
            stack.append(cur)

    return res 


if __name__ == '__main__':

    case1 = [4,1,2], [1,3,4,2]
    case2 = [2,4], [1,2,3,4]
    print(nextGreaterElement(*case1))
    print(nextGreaterElement(*case2))
