# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def maxProfit(prices: List[int]) -> int:
    
    """ My Solution """
    # total = 0
    # buy = prices[0]

    # for i, price in enumerate(prices[1:], 1):
    #     buy = min(buy, price)
    #     if i+1 < len(prices) and prices[i] > prices[i+1] or i == len(prices)-1:
    #         total += (price - buy)
    #         buy = prices[i+1] if i+1 < len(prices) else 0

    # return total

    """ Leetcode Solution """
    total = 0
    buy = prices[0]

    for price in prices[1:]:
        if buy < price:
            total += price - buy
        buy = price       

    return total


if __name__ == '__main__':


    case = [7,1,5,3,6,4]
    print(maxProfit(case))
    case = [7,1,4,5,2,6,4,3]
    print(maxProfit(case))
    case = [1,2,3,4,5,4,6]
    print(maxProfit(case))
    case = [7,6,4,3,1]
    print(maxProfit(case))