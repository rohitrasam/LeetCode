# https://leetcode.com/problems/find-the-duplicate-number/description/?envType=problem-list-v2&envId=binary-search


from typing import List


def findDuplicate(nums: List[int]) -> int:
    
    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            return idx
        nums[idx] = -nums[idx]
    
    return len(nums)


if __name__ == '__main__':

    case1 = [1,3,4,2,2]
    case2 = [3,1,3,4,2]
    case3 = [3,3,3,3,3]

    print(findDuplicate(case1))
    print(findDuplicate(case2))
    print(findDuplicate(case3))
