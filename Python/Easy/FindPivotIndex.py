# https://leetcode.com/problems/find-pivot-index/


from typing import List


def pivotIndex(nums: List[int]) -> int:
    preSum: List[int] = []

    pre = 0
    for num in nums:
        pre += num
        preSum.append(pre)
    
    
    for i in range(len(nums)):
        l_sum = 0 if i == 0 else preSum[i-1]
        r_sum = preSum[-1] - preSum[i]
        if l_sum == r_sum:
            return i
    
    return -1


if __name__ == '__main__':

    case = [1,7,3,6,5,6]
    print(pivotIndex(case))
    case = [1,2,3]
    print(pivotIndex(case))
    case = [2,1,-1]
    print(pivotIndex(case))