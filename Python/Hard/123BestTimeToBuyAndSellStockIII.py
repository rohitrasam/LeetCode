# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def maxProfit(prices: List[int]) -> int:
    profit1 = prices[0]
    profit2 = prices[1]
    buy = prices[0]

    for price in prices[1:]:
        if buy < price:
            if abs(profit1 - (price-buy)) > abs(profit2 - (price-buy)):
                profit1 = price - buy
            elif abs(profit1 - (price-buy)) < abs(profit2 - (price-buy)):
                profit2 = price - buy

        buy = min(buy, price)
    return profit1 + profit2
    



if __name__ == '__main__':


    case = [3,3,5,0,0,3,1,4]
    print(maxProfit(case))
    case = [1,2,3,4,5]
    print(maxProfit(case))
    case = [7,6,4,3,1]
    print(maxProfit(case))