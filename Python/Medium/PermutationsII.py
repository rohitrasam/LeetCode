# https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def permuteUnique(nums: List[int]) -> List[List[int]]:
    
    visited = set()

    def backTrack(subs: List[List[int]]):
        if len(subs) == 0:
            return [[]]


        perms = backTrack(subs[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:]
                p_copy.insert(i, subs[0])
                if tuple(p_copy) not in visited:
                    res.append(p_copy)
                    visited.add(tuple(p_copy))
        return res
    
    return backTrack(nums)
        
        


if __name__ == '__main__':

    case = [1,1,2]
    print(permuteUnique(case))
    case = [1,2,3]
    print(permuteUnique(case))
