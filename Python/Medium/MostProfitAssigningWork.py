# https://leetcode.com/problems/most-profit-assigning-work/description/?envType=problem-list-v2&envId=two-pointers

from typing import List


def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    sorted_diff_prof = sorted(zip(difficulty, profit), key=lambda x: x[1], reverse=True)
    worker = sorted(worker, reverse=True)

    total = 0

    for d, p in sorted_diff_prof:
        l, h = 0, len(worker)
        while l <= h and len(worker):
            m = (l + h) // 2
            if worker[m] >= d:
                total += p
                worker.pop(m)
                l, h= 0, len(worker)
            else:
                h = m - 1    

    return total



if __name__ == '__main__':

    case = [2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]
    print(maxProfitAssignment(*case))
    case = [85,47,57], [24,66,99], [40,25,25]
    print(maxProfitAssignment(*case))
    case = [4,5,2,3,6,10], [10,2,8,9,12,1], [5,4,7,2,8]
    print(maxProfitAssignment(*case))
