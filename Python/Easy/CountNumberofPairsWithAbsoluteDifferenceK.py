# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?envType=problem-list-v2&envId=hash-table


from collections import Counter
from typing import List


def countKDifference(nums: List[int], k: int) -> int:
    # pairs = 0
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if abs(nums[j] - nums[i]) == k:
    #             pairs += 1

    counter = Counter(nums)
    pairs = 0
    for num in counter:
        if num + k in counter:
            pairs += counter[num]*counter[num+k]

    return pairs


if __name__ == '__main__':

    case = [1,2,2,1], 1
    print(countKDifference(*case))
    case = [1,3], 3
    print(countKDifference(*case))
    case = [3,2,1,5,4], 2
    print(countKDifference(*case))