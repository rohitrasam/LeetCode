# https://leetcode.com/problems/contiguous-array/editorial/?envType=problem-list-v2&envId=hash-table


from typing import List


def findMaxLength(nums: List[int]) -> int:
    zero, one = 0, 0
    res = 0

    diff_index = {}

    for i, n in enumerate(nums):
        if n == 0:
            zero += 1
        else:
            one += 1

        if one - zero not in diff_index:
            diff_index[one - zero] = i
        
        if one == zero:
            res = one + zero
        else:
            idx = diff_index[one - zero]
            res = max(res, i - idx)
    
    return res


if __name__ == '__main__':
    case = [0,1]
    print(findMaxLength(case))
    case = [0,1,0]
    print(findMaxLength(case))
