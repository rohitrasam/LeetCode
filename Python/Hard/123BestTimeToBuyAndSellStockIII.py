# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def maxProfit(prices: List[int]) -> int:
    s1, s2, s3, s4 = -prices[0], float("-inf"), float("-inf"), float("-inf")

    for price in prices[1:]:
        s1 = max(s1, -price)
        s2 = max(s2, price + s1)
        s3 = max(s3, s2 - price)
        s4 = max(s4, s3 + price)

    return max(s4, 0)


if __name__ == "__main__":
    case = [3, 3, 5, 0, 0, 3, 1, 4]
    print(maxProfit(case))
    case = [1, 2, 3, 4, 5]
    print(maxProfit(case))
    case = [7, 6, 4, 3, 1]
    print(maxProfit(case))
