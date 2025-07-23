# https://leetcode.com/problems/find-k-closest-elements/solutions/?envType=problem-list-v2&envId=sliding-window


from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - k
    while l < r:
        m = (l + r) // 2
        if x - arr[m] > arr[m+k] - x:
            l = m + 1
        else:
            r = m
        
    return arr[l:l+k]


if __name__ == '__main__':

    # case = [1,2,3,4,5], 4, 3
    # print(findClosestElements(*case))
    # case = [1,1,2,3,4,5], 4, -1
    # print(findClosestElements(*case))
    case = [1,1,2,3,4,5], 4, 4
    print(findClosestElements(*case))
