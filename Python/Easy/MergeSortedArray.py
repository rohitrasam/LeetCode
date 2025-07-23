def merge(nums1: list[int], m:int, nums2: list[int], n: int) -> None:

    if not nums2 or not nums1:
        return None

    for i in range(len(nums1)-m):
        nums1.pop()

    i = 0
    j = 0

    while i < len(nums1) and j < n:
        if nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            i += 1
            j += 1
        else:
            i += 1

    while j < n:
        nums1.append(nums2[j])
        j += 1


if __name__ == '__main__':
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    n = int(input())

    merge(nums1, m, nums2, n)

    print(nums1)