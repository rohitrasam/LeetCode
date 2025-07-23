# https://leetcode.com/problems/majority-element-ii/

from collections import defaultdict
from typing import List

def majorityElement(nums: List[int]) -> List[int]:

    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

        if len(count) <= 2:
            continue

        new_count = {}
        for num, count in count.items():
            if count > 1:
                new_count[num] = count - 1
        count = new_count

    res = []
    for num in count:
        if nums.count(num) > len(nums) // 3:
            res.append(num)
    
    return res
    


    # counter = {}
    # res = []
    # for num in nums:
    #     counter[num] = counter.get(num, 0) + 1
    #     if counter[num] > len(nums) // 3:
    #         res.append(num)

    # return res

    # counter = {}

    # for num in nums:
    #     counter[num] = counter.get(num, 0) + 1
        
    # maj_elem = list(filter(lambda x: counter[x] > len(nums)/3, counter))
    # return maj_elem
    

if __name__ == '__main__':
    case1 = [3, 2, 3, 2, 4, 3]
    case2 = [1]
    case3 = [1, 2]

    print(majorityElement(case1))
    print(majorityElement(case2))
    print(majorityElement(case3))

