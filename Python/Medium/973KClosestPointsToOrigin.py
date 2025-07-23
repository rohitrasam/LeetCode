# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=problem-list-v2&envId=heap-priority-queue



import heapq
from typing import Dict, List, Tuple


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # dist: Dict[Tuple[float]] = {}
    # for x, y in points:
    #     if (x, y) in dist:
    #         dist[(x, y)][1] += 1
    #     else:
    #         dist[(x, y)] = [(x**2 + y**2)**0.5, 1]
    
    # items = list(dist.items())

    # items.sort(reverse=True, key=lambda x: x[1])
    # ans = []

    # while k > 0:
    #     closest = items.pop()
    #     while closest[1][1] != 0:
    #         ans.append(list(closest[0]))
    #         closest[1][1] -= 1
    #         k -= 1
    # return ans

    """ Neetcode Solution """

    dist: List[List[int]] = []

    for x, y in points:
        d = (x**2 + y**2)**0.5
        dist.append([d, x, y])

    heapq.heapify(dist)
    ans: List[List[int]] = []

    while k > 0:
        d, x, y = heapq.heappop(dist)
        ans.append([x, y])
        k -= 1
    
    return ans


if __name__ == '__main__':

    case = [[1,3],[-2,2]], 1
    print(kClosest(*case))
    case = [[3,3],[5,-1],[-2,4]], 2
    print(kClosest(*case))
    case = [[1,3],[-2,2],[2,-2]], 2
    print(kClosest(*case))
    case = [[2,2],[2,2],[3,3],[2,-2],[1,1]], 4
    print(kClosest(*case))