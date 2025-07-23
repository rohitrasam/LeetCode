# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/


from typing import Dict, List


def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    groups: List[List[int]] = []
    num_to_groups: Dict[int, int] = {}

    for n in sorted(nums):
        if not groups or abs(n - groups[-1][-1]) > limit:
            groups.append([])
        
        groups[-1].append(n)
        num_to_groups[n] = len(groups) - 1
    
    res: List[int] = []
    for n in nums:
        j: int = num_to_groups[n]
        res.append(groups[j].pop(0))
    
    return res

if __name__ == '__main__':

    case1 = [1,5,3,9,8], 2
    case2 = [1,7,6,18,2,1], 3
    case3 = [1,7,28,19,10], 3

    print(lexicographicallySmallestArray(*case1))
    print(lexicographicallySmallestArray(*case2))
    print(lexicographicallySmallestArray(*case3))