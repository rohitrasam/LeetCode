# https://leetcode.com/problems/matchsticks-to-square/description/

from typing import List


def makesquare(matchsticks: List[int]) -> bool:
    length = sum(matchsticks) // 4
    sides = [0] * 4

    if sum(matchsticks) / 4 != length:
        return False

    matchsticks.sort(reverse=True)

    def dfs(idx: int):
        if idx == len(matchsticks):
            return True
        
        for j in range(4):
            if sides[j] + matchsticks[idx] <= length:
                sides[j] += matchsticks[idx]
                if dfs(idx + 1):
                    return True
                sides[j] -= matchsticks[idx]
        
        return False
    
    return dfs(0)


if __name__ == '__main__':

    case = [1,1,2,2,2]
    print(makesquare(case))
    case = [3,3,3,3,4]
    print(makesquare(case))