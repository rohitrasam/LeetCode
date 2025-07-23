# https://leetcode.com/problems/combination-sum/description/?envType=problem-list-v2&envId=backtracking


from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i: int, cur: List[int], total: int):
        if total == target:
            res.append(cur[:])
            return
        if i >= len(candidates) or total > target:
            return
        
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        cur.pop()
        dfs(i + 1, cur, total)
    
    dfs(0, [], 0)
    return res

if __name__ == '__main__':

    case = [2,3,6,7], 7
    print(combinationSum(*case))
    case = [2,3,5], 8
    print(combinationSum(*case))
    case = [2], 1
    print(combinationSum(*case))
    case = [10,1,2,7,6,1,5], 8
    print(combinationSum(*case))
    case = [2,5,2,1,2], 5
    print(combinationSum(*case))
