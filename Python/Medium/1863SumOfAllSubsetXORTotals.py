# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/


from typing import List


def subsetXORSum(nums: List[int]) -> int:
    
    total = 0

    def dfs(i: int, subset: List[int]) -> None:
        if i == len(nums):
            xor = 0
            for elem in subset:
                xor ^= elem
                
            nonlocal total
            total += xor
            return
        
        subset.append(nums[i])
        dfs(i+1, subset)
        subset.pop()
        dfs(i+1, subset)
    
    dfs(0, [])
    return total


if __name__ == '__main__':

    case = [1,3]
    print(subsetXORSum(case))
    case = [5,1,6]
    print(subsetXORSum(case))
    case = [3,4,5,6,7,8]
    print(subsetXORSum(case))

