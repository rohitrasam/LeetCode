def rotate(nums: list[int], k:int):

    n = len(nums)
    k %= n

    for _ in range(k):
        temp = nums[n-1]
        nums.pop(n-1)
        nums.insert(0, temp) 

if __name__ == '__main__':
    arr = list(map(int, input().split()))

    rotate(arr, 3)
