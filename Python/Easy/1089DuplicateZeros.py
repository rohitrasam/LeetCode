# https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

from typing import List

def duplicateZeros(arr: List[int]) -> None:

    dupes = 0
    length = len(arr)-1

    for left in range(length+1):

        if left > length - dupes:
            break

        if arr[left] == 0:
            if left == length - dupes:
                arr[length] = 0
                length -= 1
                break
            dupes += 1
    
    last = length - dupes

    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + dupes] = 0
            dupes -= 1
            arr[i + dupes] = 0
        else:
            arr[i + dupes] = arr[i]
    


if __name__ == '__main__':

    case = [1,0,2,3,0,4,5,0]
    duplicateZeros(case)
    print(case)
    case = [1,2,3] 
    duplicateZeros(case)
    print(case)
