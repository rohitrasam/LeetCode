# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/?envType=problem-list-v2&envId=binary-search


from typing import List


def countPairs(nums: List[int], target: int) -> int:
    nums.sort()
    count = 0
    l = 0
    r = len(nums) - 1

    while l < r:
        s = nums[l] + nums[r]
        if s < target:
            count += r - l
            l += 1
        else:
            r -= 1

    return count

if __name__ == '__main__':

    case = [-1,1,2,3,1], 2
    print(countPairs(*case))
    case = [-6,2,5,-2,-7,-1,3], -2
    print(countPairs(*case))