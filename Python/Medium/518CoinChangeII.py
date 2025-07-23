# https://leetcode.com/problems/coin-change-ii/description/?envType=problem-list-v2&envId=dynamic-programming

from typing import Dict, List, Tuple


def change(amount: int, coins: List[int]) -> int:
    
    """ Recursion Solution Neetcode """
    # def dfs(i: int, a: int) -> int:
    #     if a == 0:
    #         return 1
    #     if i >= len(coins):
    #         return 0

    #     res = 0
    #     if a >= coins[i]:
    #         res = dfs(i+1, a)
    #         res += dfs(i, a-coins[i])

    #     return res
    
    # return dfs(0, amount)

    """ Recursion using Memoization """

    # cache: Dict[Tuple[int, int], int] = {}

    # def dfs(i: int, a: int) -> int:
    #     if a == amount:
    #         return 1
    #     if a > amount:
    #         return 0
    #     if i == len(coins):
    #         return 0
        
    #     if (i, a) in cache:
    #         return cache[(i, a)]
        
    #     cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
    #     return cache[(i, a)]

    # return dfs(0, 0)

    """ Dynamic Programming (Bottom-Up) Neetcode """
    # dp = [[0] * (len(coins) + 1) for i in range(amount+1)]
    # dp[0] = [1] * (len(coins) + 1)

    # for a in range(1, amount+1):
    #     for i in range(len(coins)-1, -1, -1):
    #         dp[a][i] = dp[a][i+1]
    #         if a - coins[i] >= 0:
    #             dp[a][i] += dp[a-coins[i]][i]
    
    # return dp[amount][0]

    """ Dynamic Programming (Space-Optimized) Neetcode """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins) - 1, -1, -1):
        nextDP = [0] * (amount + 1)
        nextDP[0] = 1

        for a in range(1, amount + 1):
            nextDP[a] = dp[a]
            if a - coins[i] >= 0:
                nextDP[a] += nextDP[a - coins[i]]
        dp = nextDP
    return dp[amount]

if __name__ == '__main__':

    case = 5, [1,2,5]
    print(f"{case = } => {change(*case)}")
    case = 6, [1,2,5]
    print(f"{case = } => {change(*case)}")
    case = 3, [2]
    print(f"{case = } => {change(*case)}")
    case = 10, [10]
    print(f"{case = } => {change(*case)}")