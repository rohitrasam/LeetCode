# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/


from typing import List

def subarraysDivByK(nums: List[int], k: int) -> int:
    counter = 0
    dictt = {}
    total = 0

    for num in nums:
        total += num
        rem = total % k
        if rem == 0:
            counter += 1
        
        if rem in dictt:
            counter += dictt[rem]

        dictt[rem] = dictt.get(rem, 0) + 1

    return counter

if __name__ == '__main__':
    case1 = [4,5,0,-2,-3,1], 5
    case2 = [5], 9
    case3 = [5, 6, 1, -2, -1, 10, -9], 8

    print(subarraysDivByK(*case1))
    print(subarraysDivByK(*case2))
    print(subarraysDivByK(*case3))