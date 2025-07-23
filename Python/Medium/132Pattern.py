# https://leetcode.com/problems/132-pattern/?envType=problem-list-v2&envId=stack

from typing import List


def find132pattern(nums: List[int]) -> bool:
    stack = []   # pair[num, minLeft], mono decreasing
    curMin = nums[0]

    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True
        
        stack.append([n, curMin])
        curMin = min(curMin, n)
    return False


if __name__ == '__main__':

    case = [1,2,3,4]
    print(find132pattern(case))
    case = [3,1,4,2]
    print(find132pattern(case))
    case = [-1,3,2,0]
    print(find132pattern(case))