def searchInsert(nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2 + (lo+hi)%2
        if target < nums[mid]:
            hi = mid- 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            return mid
    
    return lo
    


if __name__ == '__main__':

    arr = list(map(int, input().split()))
    num = int(input())
    
    print(searchInsert(arr, num))