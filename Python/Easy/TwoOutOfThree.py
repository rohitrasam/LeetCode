from typing import List


def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

    res = []
    nums1 = set(nums1)
    nums2 = set(nums2)
    nums3 = set(nums3)
    comb = nums1 | nums2 | nums3
    
    for num in comb:
        count = 0
        if num in nums1:
            count += 1
        if num in nums2:
            count += 1
        if num in nums3:
            count += 1
        if count >= 2:
            res.append(num)

    return res

if __name__ == '__main__':
    case1 = [1, 1, 3, 2], [2,3], [3]
    case2 = [3, 1], [2, 3], [1, 2]
    case3 = [1, 2, 2], [4, 3, 3], [5]
    print(twoOutOfThree(*case1))
    print(twoOutOfThree(*case2))
    print(twoOutOfThree(*case3))