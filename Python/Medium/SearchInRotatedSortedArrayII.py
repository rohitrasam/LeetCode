# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List


def search(nums: List[int], target: int) -> bool:
    return target in nums



if __name__ == '__main__':
    case1 = [2,5,6,0,0,1,2], 0
    case2 = [2,5,6,0,0,1,2], 3