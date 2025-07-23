# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=problem-list-v2&envId=hash-table


from typing import List, Set


def findMatrix(nums: List[int]) -> List[List[int]]:
    
    """ My Solution """
    i: int = 0
    seen: Set[int] = set()
    ans: List[List[int]] = []
    row: List[int] = []

    while nums:
        if nums[i] not in seen:
            row.append(nums[i])
            seen.add(nums.pop(i))
        else:
            i += 1

        if i >= len(nums):
            i = 0
            ans.append(row)
            seen = set()
            row = []

    return ans

    """ Leetcode Solution """
    # freq = [0] * (len(nums) + 1)
    # res = []
    # for num in nums:
    #     if freq[num] >= len(res):
    #         res.append([])
    #     res[freq[num]].append(num)
    #     freq[num] += 1 
    # return res 


if __name__ == '__main__':

    case = [1,3,4,1,2,3,1]
    print(findMatrix(case))
    case = [2,1,1]
    print(findMatrix(case))
    case = [1,2,3,4]
    print(findMatrix(case))

