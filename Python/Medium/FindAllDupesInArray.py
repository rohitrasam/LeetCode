from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    # res = []
    # nums_set = set()

    # for num in nums:
    #     if num not in nums_set:
    #         nums_set.add(num)
    #     else:
    #         res.append(num)
    
    # return res

    result = []
    for x in nums[:]:   # nums[:] returns a new list
        y = nums[x-1]
        if y == -1:
            result.append(x)
        else:
            nums[x-1] = -1
    return result


if __name__ == '__main__':

    case1 = [4,3,2,7,8,2,3,1]
    case2 = [1,1,2]
    case3 = [1]
    print(findDuplicates(case1))
    print(findDuplicates(case2))
    print(findDuplicates(case3))