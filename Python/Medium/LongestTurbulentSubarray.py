# https://leetcode.com/problems/longest-turbulent-subarray/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


def maxTurbulenceSize(arr: List[int]) -> int:
    if len(arr) == 1 or (len(arr) == 2 and arr[0] == arr[1]):
        return 1
    
    gt = 1 if arr[0] > arr[1] else (-1 if arr[0] < arr[1] else 0)
    l = 2 if gt != 0 else 1
    maxl = l
    for idx in range(1, len(arr) - 1):
        if arr[idx] > arr[idx+1]:
            if gt != 1:
                l += 1
                gt = 1
            else:
                maxl = max(l, maxl)
                l = 2
        elif arr[idx] < arr[idx+1]:
            if gt != -1:
                l += 1
                gt = -1
            else:
                maxl = max(l, maxl)
                l = 2
        else:
            maxl = max(l, maxl)
            l = 1
            gt = 0

    return max(maxl, l)


    """ Neetcode solution """
    l, r = 0, 1
    res, prev = 1, ""

    while r < len(arr):
        if arr[r-1] > arr[r] and prev != ">":
            res = max(res, r - l + 1)
            r += 1
            prev = ">"
        elif arr[r-1] < arr[r] and prev != "<":
            res = max(res, r - l + 1)
            r += 1
            prev = "<"
        else:
            r  = r + 1 if arr[r] == arr[r-1] else r
            l = r - 1
            prev = "="

    return res


if __name__ == '__main__':

    case = [9,4,2,10,7,8,8,1,9]
    print(maxTurbulenceSize(case))
    case = [4,8,12,16]
    print(maxTurbulenceSize(case))
    case = [100]
    print(maxTurbulenceSize(case))
    case = [1,1]
    print(maxTurbulenceSize(case))
    case = [1,2]
    print(maxTurbulenceSize(case))
    case = [1,1,2]
    print(maxTurbulenceSize(case))
    case = [0,1,1,0,1,0,1,1,0,0]
    print(maxTurbulenceSize(case))
    case = [0,8,45,88,48,68,28,55,17,24]
    print(maxTurbulenceSize(case))
    case = [100,100,100]
    print(maxTurbulenceSize(case))