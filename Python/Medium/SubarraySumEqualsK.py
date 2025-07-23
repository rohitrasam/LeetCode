# https://leetcode.com/problems/subarray-sum-equals-k/submissions/1491488777/

from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    counter = 0
    dictt = {}
    total = 0

    for num in nums:
        total += num
        if total == k:
            counter += 1

        if total - k in dictt:
            counter += dictt[total - k]
        
        dictt[total] = dictt.get(total, 0) + 1
    
    return counter


if __name__ == '__main__':

    case1 = [1,1,1], 2
    case2 = [1,2,3], 3
    case3 = [1, -1, 1, 1, 1, 3], 3

    print(subarraySum(*case1))
    print(subarraySum(*case2))
    print(subarraySum(*case3))