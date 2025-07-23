# https://leetcode.com/problems/find-unique-binary-string/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def findDifferentBinaryString(nums: List[str]) -> str:
    n = len(nums[0])
    nums = set(nums)
    
    def dfs(unique: List[str]) -> str | None:
        if len(unique) == n:
            if "".join(unique) not in nums:
                return "".join(unique)
            return
        
        for bi in ["0", "1"]:
            unique.append(bi)
            res = dfs(unique)
            if res:
                return res
            unique.pop()

    return dfs([])


if __name__ == '__main__':

    case = ["01","10"]
    print(findDifferentBinaryString(case))
    case = ["00","01"]
    print(findDifferentBinaryString(case))
    case = ["111","011","001"]
    print(findDifferentBinaryString(case))
    
