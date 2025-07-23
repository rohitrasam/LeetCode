# https://leetcode.com/problems/non-decreasing-subsequences/description/?envType=problem-list-v2&envId=backtracking


from typing import List


def findSubsequences(nums: List[int]) -> List[List[int]]:

    """ My partial solution """
    ans = set()

    def dfs(i: int, curr: List[int]):
        if len(curr) >= 2 and tuple(curr) not in ans:
            ans.add(tuple(curr))
        if i >= len(nums):
            return
        
        if curr and curr[-1] <= nums[i]:
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()

        dfs(i+1, curr)
    
    for idx, num in enumerate(nums):
        dfs(idx+1, [num])

    return list(map(list, ans))
        

if __name__ == '__main__':

    case = [4,6,7,7]
    print(findSubsequences(case))
    case = [4,6,7,8]
    print(findSubsequences(case))
    case = [4,6,7,5]
    print(findSubsequences(case))
    case = [4,4,3,2,1]
    print(findSubsequences(case))
