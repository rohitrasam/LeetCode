# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def maxProfit(prices: List[int]) -> int:

    """ My Soultion """
    profit = 0
    buy = prices[0]
    for price in prices[1:]:
        buy = min(buy, price)
        profit = max(profit, price - buy)
    
    return profit

    # """ Leetcode/Youtube Solution"""
    # max_profit = 0
    # cheapest = prices[0]

    # for price in prices:
    #     if price < cheapest:
    #         cheapest = price
    #     else:
    #         profit = price - cheapest
    #         if  profit > max_profit:
    #             max_profit = profit
        

    # return max_profit


if __name__ == '__main__':
    stocks = list(map(int, input().split()))


    print(maxProfit(stocks))
