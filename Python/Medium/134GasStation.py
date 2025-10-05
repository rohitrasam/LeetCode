# https://leetcode.com/problems/gas-station/description/?envType=problem-list-v2&envId=greedy

from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    
    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
            total = 0
            res = i + 1

    return res


if __name__ == "__main__":
    case = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
    print(canCompleteCircuit(*case))
    case = [2, 3, 4], [3, 4, 3]
    print(canCompleteCircuit(*case))
    case = [1,6,3,4,5], [3,4,5,1,2]
    print(canCompleteCircuit(*case))
