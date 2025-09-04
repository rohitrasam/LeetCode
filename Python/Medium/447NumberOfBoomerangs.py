# https://leetcode.com/problems/number-of-boomerangs/description/?envType=problem-list-v2&envId=hash-table

from collections import defaultdict
from typing import List, DefaultDict


def dist(a: List[int], b: List[int]) -> int:

    return (b[0] - a[0])**2 + (b[1] - a[1])**2

def numberOfBoomerangs(points: List[List[int]]) -> int:
    
    ans = 0

    for x in points:
        hashmap: DefaultDict[int, int] = defaultdict(int)
        for y in points:
            if x[0] == y[0] and x[1] == y[1]:
                continue
            d = dist(x, y)
            hashmap[d] += 1

        for cnt in hashmap.values():
            ans += (cnt * (cnt-1))

    return ans



if __name__ == '__main__':

    case = [[0,0],[1,0],[2,0]]
    print(numberOfBoomerangs(case))
    case = [[1,1],[2,2],[3,3]]
    print(numberOfBoomerangs(case))
    case = [[1,1]]
    print(numberOfBoomerangs(case))
