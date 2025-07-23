def summaryRange(nums: list[int]) -> list[str]:
    if not nums:
        return nums
    
    last, start = 0, 0
    res = []

    while start < len(nums)-1:
        if nums[start+1] - nums[start] == 1:
            start += 1
        else:
            res.append(f"{nums[last]}->{nums[start]}" if last != start else f"{nums[last]}")
            last = start+1
            start += 1
    res.append(f"{nums[last]}->{nums[start]}" if last != start else f"{nums[last]}")

    
    return res




if __name__ == '__main__':
    arr = list(map(int, input().split()))

    print(summaryRange(arr))