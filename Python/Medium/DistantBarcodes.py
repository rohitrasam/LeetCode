# https://leetcode.com/problems/distant-barcodes/description/

import heapq
from typing import List


def rearrangeBarcodes(barcodes: List[int]) -> List[int]:

    count = {}
    for code in barcodes:
        count[code] = count.get(code, 0) + 1
    
    pq = [(-val, key) for key, val in count.items()]
    ans = []

    heapq.heapify(pq)
    while pq:
        freq1, code1 = heapq.heappop(pq)
        if pq:
            freq2, code2 = heapq.heappop(pq)
            ans.append(code1)
            ans.append(code2)
            if freq1 + 1 < 0:
                freq1 += 1
                heapq.heappush(pq, (freq1, code1))
            if freq2 + 1< 0:
                freq2 += 1  
                heapq.heappush(pq, (freq2, code2))
        else:
            ans.append(code1)
    
    return ans
    

if __name__ == '__main__':

    case1 = [1,1,1,2,2,2]
    case2 = [1,1,1,1,2,2,3,3]
    case3 = [2,1,1]
    # print(rearrangeBarcodes(case1))
    # print(rearrangeBarcodes(case2))
    print(rearrangeBarcodes(case3))