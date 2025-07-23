def moveZeroes(nums: list[int]) -> None:
    # i = 0
    # j = len(nums)-1
    # while i < j:
    #     if nums[i] == 0:
    #         zero = nums.pop(i)
    #         nums.append(zero)
    #         j -= 1 
    #     else:
    #         i += 1

    l = 0

    for r in range(1, len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1


if __name__ == '__main__':
    n = list(map(int, input().split()))

    moveZeroes(n)
    print(n)