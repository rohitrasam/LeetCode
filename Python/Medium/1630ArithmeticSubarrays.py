# https://leetcode.com/problems/arithmetic-subarrays/description/?envType=problem-list-v2&envId=hash-table


from typing import List


def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    ans: List[bool] = []

    for i in range(len(l)):
        seq = sorted(nums[l[i]:r[i]+1])
        diff = seq[1] - seq[0]
        stop = 2
        for j in range(2, len(seq)):
            if seq[j] - seq[j-1] != diff:
                ans.append(False)
                stop = j
                break
        if (stop < len(seq) and seq[stop] - seq[stop-1] == diff) or (len(seq) == 2 and seq[1] - seq[0] == diff):
            ans.append(True)
    
    return ans





if __name__ == '__main__':


    case = [4,6,5,9,3,7], [0,0,2], [2,3,5]
    print(checkArithmeticSubarrays(*case))
    case = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]
    print(checkArithmeticSubarrays(*case))