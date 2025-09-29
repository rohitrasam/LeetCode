# https://leetcode.com/problems/largest-divisible-subset/?envType=problem-list-v2&envId=dynamic-programming

from typing import List


def largestDivisibleSubset(nums: List[int]) -> List[int]:

    

if __name__ == '__main__':

    case = [1, 2, 3]
    print(largestDivisibleSubset(case))
    case = [1, 2, 4, 8]
    print(largestDivisibleSubset(case))
    case = [3, 4, 16, 8]
    print(largestDivisibleSubset(case))
    case = [1]
    print(largestDivisibleSubset(case))
    case = [1, 3, 6, 24]
    print(largestDivisibleSubset(case))