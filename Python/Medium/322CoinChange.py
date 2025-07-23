# https://leetcode.com/problems/coin-change/description/?envType=problem-list-v2&envId=dynamic-programming

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    
    """ BackTracking """
    # def dfs(total: int):
    #     if total == 0:
    #         return 0
        
    #     res = 10e9

    #     for coin in coins:
    #         if total - coin >= 0:
    #             res = min(res, 1 + dfs(total - coin))
        
    #     return res


    # minCoins = dfs(amount)
    # return -1 if minCoins == 10e9 else minCoins


    """ Dynamic Programming """

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for amount in range(1, amount + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    
    return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':


    case = [1,2,5], 11
    print(coinChange(*case))
    case = [2], 3
    print(coinChange(*case))
    case = [1], 0
    print(coinChange(*case))