# https://leetcode.com/problems/sort-an-array/description/

from typing import List


def sortArray(nums: List[int]) -> List[int]:
    if len(nums) > 1:
        left_arr = nums[:len(nums)//2]
        right_arr = nums[len(nums)//2:]

        sortArray(left_arr)
        sortArray(right_arr)

        i = j = k =0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            nums[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            nums[k] = right_arr[j]
            j += 1
            k += 1

    return nums


if __name__ == '__main__':

    # case = [5,2,3,1]
    # print(sortArray(case))
    case = [-1,2,-8,-10]
    print(sortArray(case))
    case = [5,1,1,2,0,0]
    print(sortArray(case))