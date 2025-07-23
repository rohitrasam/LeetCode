# https://leetcode.com/problems/shopping-offers/?envType=problem-list-v2&envId=backtracking

from typing import List


def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    pass


if __name__ == '__main__':

    case = [2,5], [[3,0,5],[1,2,10]], [3,2]
    print(shoppingOffers(*case))
    case = [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
    print(shoppingOffers(*case))