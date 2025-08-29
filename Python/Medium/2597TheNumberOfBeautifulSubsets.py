# https://leetcode.com/problems/the-number-of-beautiful-subsets/description/?envType=problem-list-v2&envId=backtracking


from collections import defaultdict
from typing import Dict, List


def beautifulSubsets(nums: List[int], k: int) -> int:
    
    
    def bt(i: int, count: Dict[int, int]) -> int:
        if i == len(nums):
            return 1
        
        res = bt(i+1, count)   # skip nums[i]
        
        if not count[nums[i] + k] and not count[nums[i] - k]:
            # include nums[i]
            count[nums[i]] += 1
            res += bt(i + 1, count)
            count[nums[i]] -= 1
        
        return res

    return bt(0, defaultdict(int)) - 1



if __name__ == '__main__':

    case = [2,4,6], 2
    print(beautifulSubsets(*case))
    case = [1], 1
    print(beautifulSubsets(*case))
    case = [2,3,4,6], 3
    print(beautifulSubsets(*case))
