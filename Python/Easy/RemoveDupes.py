def removeDuplicates(nums: list[int]) -> int:

    """
        1. Start with i = 0, j = i + 1
        2. if nums[i] == nums[j] -> remove nums[j]
        3. else i += 1, j += 1 

    """
    
    i = 0
    j =i + 1

    while i < len(nums)-1 and j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)
        else:
            i += 1
            j += 1
        
    return len(nums)

    
if __name__ == '__main__':
    nums = list(map(int, input().split()))


    print(removeDuplicates(nums))