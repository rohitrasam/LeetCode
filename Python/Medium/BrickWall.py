# https://leetcode.com/problems/brick-wall/description/?envType=problem-list-v2&envId=hash-table

from typing import List


def leastBricks(wall: List[List[int]]) -> int:
    gaps = {0: 0}

    for r in wall:
        total = 0
        for b in r[:-1]:
            total += b
            gaps[total] = 1 + gaps.get(total, 0)
    
    # min_bricks = float('inf')
    # for gap in gaps:
    #     min_bricks = min(len(wall) - gaps[gap], min_bricks)
            
    return len(wall) - max(gaps.values())


if __name__ == '__main__':

    case = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(leastBricks(case))
    case = [[1],[1],[1]]
    print(leastBricks(case))
