# https://leetcode.com/problems/average-waiting-time/description/

from typing import List


def averageWaitingTime(customers: List[List[int]]) -> float:
    pass


if __name__ == "__main__":
    case = [[1, 2], [2, 5], [4, 3]]
    print(averageWaitingTime(case))
    case = [[5, 2], [5, 4], [10, 3], [20, 1]]
    print(averageWaitingTime(case))
