from typing import List

def checkSubarraySum(nums: List[int], k: int) -> bool:
    dictt = {0 :-1}
    total = 0

    for i in range(len(nums)):
        total += nums[i] % k
        if total in dictt:
            if i - dictt[total] >= 2:
                return True
        else:
            dictt[total] = i
    return False


if __name__ == '__main__':

    # case1 = [23,2,4,6,7], 6
    # case2 = [23,2,6,4,7], 6
    # case3 = [23,2,6,4,7], 13
    # case4 = [10, 1, 11, 2, 6, 3], 5
    # case5 = [11, 1, 11, 2, 6, 3], 5
    case6 = [5,0,0,0], 3

    # print(checkSubarraySum(*case1))
    # print(checkSubarraySum(*case2))
    # print(checkSubarraySum(*case3))
    # print(checkSubarraySum(*case4))
    # print(checkSubarraySum(*case5))
    print(checkSubarraySum(*case6))