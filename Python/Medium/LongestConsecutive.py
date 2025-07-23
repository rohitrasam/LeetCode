from typing import List

def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) not in numSet:
            length = 0
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    
    return longest
    
if __name__ == '__main__':

    case1 = [100,4,200,1,3,2]
    case2 = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(case1))
    print(longestConsecutive(case2))
