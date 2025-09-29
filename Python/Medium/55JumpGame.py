# https://leetcode.com/problems/jump-game/?envType=problem-list-v2&envId=dynamic-programming


from typing import List


def canJump(nums: List[int]) -> bool:

    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    
    return goal == 0


    # def bt(i: int) -> bool:
    #     if i == len(nums) - 1:
    #         return True

    #     for step in range(1, nums[i]+1):
    #         if bt(i+step):
    #             return True
            
    #     return False


    # return bt(0)

if __name__ == '__main__':

    case = [2,3,1,1,4]
    print(canJump(case))

    case = [3,2,1,0,4]
    print(canJump(case))

    case = [0, 1, 3, 5, 1]
    print(canJump(case))

    case = [2, 1, 1, 4, 5, 1]
    print(canJump(case))