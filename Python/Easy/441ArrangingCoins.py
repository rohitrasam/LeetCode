# https://leetcode.com/problems/arranging-coins/description/?envType=problem-list-v2&envId=binary-search


def arrangeCoins(n: int) -> int:

    """ Leetcode solution - TC: O(n) """
    # stairs = 0

    # i = 1

    # while n >= 0:
    #     n -= i

    #     if n >= 0:
    #         stairs += 1
        
    #     i += 1
    
    # return stairs

    """ Leetcode Solution - TC: O(log(n))"""
    stairs = 0

    start = 1
    end = (n + 1) // 2

    while start <= end:
        mid = (start + end) // 2
        if (mid * (mid + 1)) // 2 <= n:
            stairs = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return stairs



if __name__ == '__main__':

    case = 5 
    print(arrangeCoins(case))
    case = 8 
    print(arrangeCoins(case))