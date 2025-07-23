def removeElement(nums: list[int], val: int) -> int:

    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    
    return len(nums)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    v = int(input())

    print(removeElement(nums, v))