from typing import List

def sortColors(nums: List[int]) -> None:
    
    if len(nums) == 1:
        return None

    l, r = 0, len(nums) - 1
    i = 0

    def swap(i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    while i <= r:
        if nums[i] == 0:
            swap(l, i)    
            l += 1
        elif nums[i] == 2:
            swap(i, r)
            r -= 1
            i -= 1
        i += 1

if __name__ == '__main__':
    # case1 = [2,0,2,1,1,0]
    # case2 = [2, 0, 1]
    case2 = [2, 2]

    # sortColors(case1)
    # print(case1)
    sortColors(case2)
    print(case2)