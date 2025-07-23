# https://leetcode.com/problems/combinations/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def combine(n: int, k: int) -> List[List[int]]:

    res = []
    combo = []

    def backTrack(i: int):
        if len(combo) == k:
            res.append(combo[:])
            return
        if i > n:
            return
        combo.append(i)
        backTrack(i+1)

        combo.pop()
        backTrack(i+1)

    backTrack(1)
    return res


if __name__ == '__main__':

    case = 4, 2
    print(combine(*case))
    case = 4, 3
    print(combine(*case))
    case = 1, 1
    print(combine(*case))
