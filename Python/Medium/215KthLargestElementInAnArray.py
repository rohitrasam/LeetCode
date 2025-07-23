# https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=problem-list-v2&envId=heap-priority-queue

import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    nums = list(map(lambda x: -x, nums))
    heapq.heapify(nums)

    while k > 1:
        heapq.heappop(nums)
        k -= 1
    
    return -heapq.heappop(nums)


if __name__ == '__main__':

    case = [3,2,1,5,6,4], 2
    print(findKthLargest(*case))
    case = [3,2,3,1,2,4,5,5,6], 4
    print(findKthLargest(*case))
