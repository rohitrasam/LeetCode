# https://leetcode.com/problems/maximum-strength-of-a-group/description/?envType=problem-list-v2&envId=backtracking


from typing import List


def maxStrength(nums: List[int]) -> int:
    max_ans = nums[0]

    def bt(i: int, curr_ans: int):
        if i >= len(nums):
            nonlocal max_ans
            max_ans = max(max_ans, curr_ans)
            return

        bt(i + 1, curr_ans * nums[i])
        bt(i + 1, curr_ans)

    bt(0, 1)

    return max_ans

if __name__ == "__main__":
    case = [3, -1, -5, 2, 5, -9]
    # print(maxStrength(case))
    case = [-4, -5, -4]
    # print(maxStrength(case))
    case = [0,-1]
    print(maxStrength(case))
    case = [0,-1, -2]
    print(maxStrength(case))
