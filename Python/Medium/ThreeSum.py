from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:

    nums.sort()
    res = []
    for idx in range(len(nums)):
        if idx > 0 and nums[idx-1] == nums[idx]:
            continue

        low = idx + 1
        high = len(nums)-1
        target = -nums[idx]
        while low < high:
            if nums[low] + nums[high] < target:
                low += 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                res.append([nums[idx], nums[low], nums[high]])
                low += 1
                while nums[low] == nums[low-1] and low < high:  # skip over remaining duplicates
                    low += 1

    return res

if __name__ == '__main__':
    case1 = [-1,0,1,2,-1,-4]
    case2 = [0,1,1]
    case3 = [0,0,0]


    print(threeSum(case1))
    print(threeSum(case2))
    print(threeSum(case3))