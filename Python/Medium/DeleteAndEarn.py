from typing import List

def deleteAndEarn(nums: List[int]) -> int:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    nums = sorted(list(set(nums)))
    earn1, earn2 = 0, 0
    
    for i in range(len(nums)):
        currEarn = nums[i] * count[nums[i]]
        if i > 0 and nums[i] - 1 == nums[i-1]:
            temp = earn2
            earn2 = max(currEarn + earn1, earn2)
            earn1 = temp
        else:
            temp = earn2
            earn2 = currEarn + earn2
            earn1 = temp

    return earn2

if __name__ == '__main__':
    
    case1 = [2, 2, 3, 3, 3, 4]
    print(deleteAndEarn(case1))
