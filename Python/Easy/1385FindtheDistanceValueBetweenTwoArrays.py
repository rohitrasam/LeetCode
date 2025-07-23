# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/?envType=problem-list-v2&envId=binary-search


from typing import List


def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:

    arr2.sort()
    dist = 0

    for num in arr1:
        start = 0
        end = len(arr2)-1
        while start <= end:
            mid = (start + end) // 2
            if abs(num - arr2[mid]) <= d:
                dist += 1
                break
            elif num < arr2[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return len(arr1) - dist


if __name__ == '__main__':

    case = [4,5,8], [10,9,1,8], 2
    print(findTheDistanceValue(*case))
    case = [1,4,2,3], [-4,-3,6,10,20,30], 3
    print(findTheDistanceValue(*case))
    case = [2,1,100,3], [-5,-2,10,-3,7], 6
    print(findTheDistanceValue(*case))
    case = [-3,10,2,8,0,10], [-9,-1,-4,-9,-8], 9
    print(findTheDistanceValue(*case))