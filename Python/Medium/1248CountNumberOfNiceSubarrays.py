# https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=problem-list-v2&envId=sliding-window


from typing import List


def isOdd(num: int) -> bool:
    return num % 2


def atMost(nums: List[int], k: int) -> int:
    win_size, sa, start = 0, 0, 0

    for end in range(len(nums)):
        win_size += isOdd(nums[end])

        while win_size > k:
            win_size -= isOdd(nums[start])
            start += 1

        sa += end - start + 1

    return sa


def numberOfSubarrays(nums: List[int], k: int) -> int:
    return atMost(nums, k) - atMost(nums, k - 1)


if __name__ == "__main__":
    case = [1, 1, 2, 1, 1], 3
    print(numberOfSubarrays(*case))
    case = [2, 4, 6], 1
    print(numberOfSubarrays(*case))
    case = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2
    print(numberOfSubarrays(*case))
    case = [2, 2, 2, 1, 2, 2, 1, 2, 1, 2], 2
    print(numberOfSubarrays(*case))
