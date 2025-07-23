def containsNearbyDuplicate(nums: list[int],k: int) -> bool:
    dupes = {}

    for idx, num in enumerate(nums):
        if num in dupes and abs(dupes[num] - idx) <= k:
            return True
        else:
            dupes[num] = idx
    
    return False




if __name__ == '__main__':
    arr = list(map(int, input().split()))
    k = int(input())
    print(containsNearbyDuplicate(arr, k))