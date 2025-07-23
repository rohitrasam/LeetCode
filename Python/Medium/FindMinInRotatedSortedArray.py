from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    res = nums[l]

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        
        m = (l + r) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
        
    return res

if __name__ == '__main__':
    case1 = [3,4,5,1,2]
    case2 = [4,5,6,7,0,1,2]
    case3 = [11,13,15,17]
    
    print(findMin(case1))
    print(findMin(case2))
    print(findMin(case3))