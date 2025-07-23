from typing import List

def nextGreaterElements(nums: List[int]) -> List[int]:
    stack = []
    res = [-1] * len(nums)

    for idx in range(len(nums)*2):
        while stack and nums[idx % len(nums)] > nums[stack[-1]]:
            res[stack.pop()] = nums[idx % len(nums)]
        stack.append(idx%len(nums))
    return res

if __name__ == '__main__':

    case1 = [1, 2, 1]
    case2 = [1, 2, 3, 4, 3]

    print(nextGreaterElements(case1))
    print(nextGreaterElements(case2))
