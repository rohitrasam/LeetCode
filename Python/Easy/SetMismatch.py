# https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=hash-table


from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    count = [0] * len(nums)

    for num in nums:
        count[num-1] += 1
    
    ans = []
    for idx, c in enumerate(count):
        if c > 1 or c == 0:
            ans.append(idx+1)

    return ans

if __name__ == '__main__':

    case = [1,2,2,4]
    print(findErrorNums(case))
    case = [1,1]
    print(findErrorNums(case))
