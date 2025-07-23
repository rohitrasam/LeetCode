# https://leetcode.com/problems/koko-eating-bananas/description/


import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:

    l, r = 1, max(piles)
    res = r
    while l <= r:
        m = (r + l) // 2
        time = sum(math.ceil(pile / m) for pile in piles)
        if time <= h:
            res = min(res, m)
            r = m - 1
        else:
            l = m + 1
    
    return res

if __name__ == '__main__':

    case1 = [3,6,7,11], 8
    case2 = [30,11,23,4,20], 5
    case3 = [30,11,23,4,20], 6

    print(minEatingSpeed(*case1))
    print(minEatingSpeed(*case2))
    print(minEatingSpeed(*case3))

