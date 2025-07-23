from collections import Counter

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    
    """ My solution """
    # nums2, nums1 = (nums2, nums1) if len(nums2) < len(nums1) else (nums1, nums2)
    # counter = Counter(nums1)
    
    # # for num in nums1:
    # #     if num in counter:
    # #         counter[num] += 1
    # #     else:
    # #         counter[num] = 1

    # ans = []
    # for num in nums2:
    #     if num in counter and counter[num] > 0:
    #         ans.append(num)
    #         counter[num] -= 1
    # return ans

    """ Solution 1 """
    ans = []
    for num in nums1:
        if num in nums2:
            ans.append(num)
            nums2.remove(num)

    return ans

if __name__ == '__main__':

    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    print(intersection(nums1, nums2))
