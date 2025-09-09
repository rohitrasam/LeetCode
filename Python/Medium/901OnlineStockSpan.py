# https://leetcode.com/problems/online-stock-span/description/?envType=problem-list-v2&envId=stack

from collections import deque
from typing import Deque, Tuple


class StockSpanner:
    def __init__(self):
        self.stocks: Deque[Tuple[int, int]] = deque()

    def next(self, price: int) -> int:
        span = 1
        while self.stocks and price >= self.stocks[0][0]:
            span += self.stocks[0][1]
            self.stocks.popleft()
        
        self.stocks.appendleft((price, span))
        return span
        


if __name__ == "__main__":
    stockSpanner = StockSpanner()

    print(stockSpanner.next(100))  # return 1
    print(stockSpanner.next(80))  # return 1
    print(stockSpanner.next(60))  # return 1
    print(stockSpanner.next(70))  # return 2
    print(stockSpanner.next(60))  # return 1
    print(
        stockSpanner.next(75)
    )  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
    print(stockSpanner.next(85))  # return 6
