from collections import defaultdict

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:

    # Solution 1
    # ans = []
    # dc = defaultdict(lambda: 0)
    # for a in nums1:
    #     dc[a] = 1
    # nums2 = set(nums2)

    # for a in nums2:
    #     if dc[a] == 1:
    #         ans.append(a)
    # return ans

    """My Solution"""
    # ans = set()
    # nums2, nums1 = (nums2, nums1) if len(nums2) < len(nums1) else (nums1, nums2)

    # for num in nums2:
    #     if num in nums1:
    #         ans.add(num)
    
    # return list(ans)

    nums1 = set(nums1)
    nums2 = set(nums2)
    ans = []

    for num in nums1:
        if num in nums2:
            ans.append(num)

    return ans

    # one liner solution
    # return list(set(nums2) & set(nums2))



if __name__ == '__main__':

    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    print(intersection(nums1, nums2))


