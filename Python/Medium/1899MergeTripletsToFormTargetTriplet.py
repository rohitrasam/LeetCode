# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/?envType=problem-list-v2&envId=greedy

from typing import List, Set


def mergeTriplets(triplets: List[List[int]], target: List[int]) -> bool:
    good: Set[int] = set()

    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        for i, v in enumerate(t):
            if v == target[i]:
                good.add(i)
        
    return len(good) == 3


if __name__ == "__main__":
    case = [[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]
    print(mergeTriplets(*case))
    case = [[3, 4, 5], [4, 5, 6]], [3, 2, 5]
    print(mergeTriplets(*case))
    case = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]
    print(mergeTriplets(*case))
