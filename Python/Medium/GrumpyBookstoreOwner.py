# https://leetcode.com/problems/grumpy-bookstore-owner/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    
    l = 0
    window = max_win = 0
    statisfied = 0
    for r in range(len(customers)):
        if grumpy[r]:
            window += customers[r]
        else:
            statisfied += customers[r]
        
        if r - l + 1 > minutes:
            if grumpy[l]:
                window -= customers[l]
            l += 1
        max_win = max(window, max_win)

    return statisfied + max_win


if __name__ == '__main__':

    case = [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3
    print(maxSatisfied(*case))
    case = [1], [0], 1
    print(maxSatisfied(*case))
    case = [1,1,2,1,3,7,1], [1,1,0,1,0,1,1], 4
    print(maxSatisfied(*case))
    case = [1,7,2,1,3,2,1], [1,1,0,1,0,1,1], 4
    print(maxSatisfied(*case))