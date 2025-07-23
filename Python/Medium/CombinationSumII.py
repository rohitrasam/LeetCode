# https://leetcode.com/problems/combination-sum-ii/?envType=problem-list-v2&envId=backtracking

from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    
    res = []
    candidates.sort()

    def backTrack(i: int, curr: List[int], total: int) -> None:
        if total == target:
            res.append(curr[:])
            return
        
        if i >= len(candidates) or total > target:
            return

        curr.append(candidates[i])
        backTrack(i+1, curr, total + candidates[i])
        curr.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        backTrack(i+1, curr, total)

    backTrack(0, [], 0)
    return res

if __name__ == '__main__':

    case = [10,1,2,7,6,1,5], 8
    print(combinationSum2(*case))
    case = [2,5,2,1,2], 5
    print(combinationSum2(*case))
