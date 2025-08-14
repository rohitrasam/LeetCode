# https://leetcode.com/problems/average-waiting-time/description/

from typing import Dict, List


def averageWaitingTime(customers: List[List[int]]) -> float:
    
    waiting: List[int] = [(customers[0][0] + customers[0][1])]
    total = customers[0][1]
    for (arrival, wait) in customers[1:]:
        if arrival < waiting[-1]:
            waiting.append(waiting[-1] + wait)
        else:
            waiting.append(arrival + wait)
        total += waiting[-1] - arrival
    
    return total / len(customers)

if __name__ == "__main__":
    case = [[1, 2], [2, 5], [4, 3]]
    print(averageWaitingTime(case))
    case = [[5, 2], [5, 4], [10, 3], [20, 1]]
    print(averageWaitingTime(case))
