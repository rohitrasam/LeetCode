# https://leetcode.com/problems/sliding-window-maximum/description/?envType=problem-list-v2&envId=sliding-window

from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    
    out = []
    q = []
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.pop(0)
        
        if r + 1 > l:
            out.append(nums[q[0]])
            l += 1

        r += 1

    return out
    
if __name__ == '__main__':

    case = [1,3,-1,-3,5,3,6,7], 3
    print(maxSlidingWindow(*case))
    case = [1,3,-1,-3,5,3,6,7], 4
    print(maxSlidingWindow(*case))
    case = [1], 1
    print(maxSlidingWindow(*case))
    case = [1,-1,2], 1
    print(maxSlidingWindow(*case))
    case = [1,-1,2], 2
    print(maxSlidingWindow(*case))
    case = [1,2,-1], 1
    print(maxSlidingWindow(*case))
    case = [1,2,-1], 2
    print(maxSlidingWindow(*case))
