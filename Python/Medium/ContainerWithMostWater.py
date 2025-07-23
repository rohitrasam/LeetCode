from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = -1

    while left < right:
        max_area = max((right-left)*min(height[left], height[right]), max_area )
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    
    return max_area



if __name__ == '__main__':
    
    case1 = [1,8,6,2,5,4,8,3,7]
    case2 = [1, 1]
    case3 = [4,4,2,11,0,11,5,11,13,8]

    print(maxArea(case1))
    print(maxArea(case2))
    print(maxArea(case3))