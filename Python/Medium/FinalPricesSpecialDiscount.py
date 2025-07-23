# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=problem-list-v2&envId=stack


from typing import List


def finalPrices(prices: List[int]) -> List[int]:
    # stack = []

    # for idx, price in enumerate(prices):
    #     while stack and price <= prices[stack[-1]]:
    #         prev_idx = stack.pop()
    #         discount = prices[prev_idx] - price
    #         prices[prev_idx] = discount
    #     stack.append(idx)

    # return prices
    
    n = len(prices)
    for i in range(n-1):
        for j in range(i+1, n):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break
    
    return prices


if __name__ == '__main__':

    case = [8,4,6,2,3]
    print(finalPrices(case))
    case = [1,2,3,4,5]
    print(finalPrices(case))
    case = [10,1,1,6]
    print(finalPrices(case))

