# https://leetcode.com/problems/jump-game-ii/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def jump(nums: List[int]) -> int:
    
    jumps = [float("inf")] * len(nums)
    jumps[-1] = 0

    for i in range(len(nums)-2, -1, -1):
        if nums[i] == 0:
            continue
        jumps[i] = min(jumps[i:i+nums[i]+1]) + 1

    return jumps[0]
    


if __name__ == "__main__":
    case = [2, 3, 1, 1, 4]
    print(jump(case))
    case = [2, 3, 0, 1, 4]
    print(jump(case))
    case = [0]
    print(jump(case))
    case = [2, 1, 1, 1, 1]
    print(jump(case))
