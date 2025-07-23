# https://leetcode.com/problems/closest-dessert-cost/description/?envType=problem-list-v2&envId=backtracking


from typing import List


def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    
    best = float("inf")

    def dfs(idx: int, cost: int) -> None:
        if idx >= len(toppingCosts):
            nonlocal best
            if abs(target - cost) == abs(best - cost):
                best = min(cost, best)
            else:
                best = min(best, cost, key=lambda cst: abs(target - cst))

            return
        
        dfs(idx+1, cost)
        dfs(idx+1, cost + toppingCosts[idx])
        dfs(idx+1, cost + 2 * toppingCosts[idx])
    
    for bc in baseCosts:
        dfs(0, bc)

    return best

if __name__ == '__main__':


    case = [1,7], [3,4], 10
    print(closestCost(*case))
    case = [2,3], [4,5,100], 18
    print(closestCost(*case))
    case = [3,10], [2,5], 9
    print(closestCost(*case))