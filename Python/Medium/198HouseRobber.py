# https://leetcode.com/problems/house-robber/


from typing import List


def rob(nums: List[int]) -> int:

    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp


    return rob2



if __name__ == '__main__':

    case = [1,2,3,1]
    print(rob(case))    
    case = [2,7,9,3,1]
    print(rob(case))