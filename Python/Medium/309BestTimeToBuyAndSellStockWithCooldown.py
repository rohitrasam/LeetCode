# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import Dict, List, Tuple


def maxProfit(prices: List[int]) -> int:

    """ Neetcode solution """
    dp: Dict[Tuple[int, bool], int] = {}
    
    def dfs(i: int, buying: bool) -> int:
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]


        cooldown = dfs(i+1, buying)
        if buying:
            buy = dfs(i+1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)

        return dp[(i, buying)]

    return dfs(0, True)

    """ Solution: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/comments/1725067/ """
    


if __name__ == '__main__':

    case = [1,2,3,0,2]
    print(f"{maxProfit(case)=}")
    case = [1]
    print(f"{maxProfit(case)=}")
    case = [7,1,5,3,6,4]
    print(f"{maxProfit(case)=}")
    case = [7,1,4,5,2,6,4,3]
    print(f"{maxProfit(case)=}")
    case = [1,2,3,4,5,4,6]
    print(f"{maxProfit(case)=}")
    case = [7,6,4,3,1]
    print(f"{maxProfit(case)=}")
