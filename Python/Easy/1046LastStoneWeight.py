# https://leetcode.com/problems/last-stone-weight/description/?envType=problem-list-v2&envId=heap-priority-queue

from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    if len(stones) == 1:
        return stones[0]
    
    stones = list(map(lambda x: -x, stones))
    heapq.heapify(stones)
        
    while stones:
        first, second = -heapq.heappop(stones), -heapq.heappop(stones)
        smashed = abs(first - second)
        if smashed != 0:
            heapq.heappush(stones, -smashed)
        if len(stones) == 1:
            return -stones[0]
    
    return 0

if __name__ == '__main__':

    case = [2,7,4,1,8,1]
    print(lastStoneWeight(case))
    case = [1]
    print(lastStoneWeight(case))
