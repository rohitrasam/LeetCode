from typing import List

def trap(height: List[int]) -> int:
    l, r = 0, len(height)-1
    maxL, maxR  = height[l], height[r]

    units = 0

    while l < r:

        if height[l] < height[r]:
            units += max(maxL - height[l], 0)
            maxL = max(maxL, height[l])
            l += 1
        else:
            units += max(maxR - height[r], 0)
            maxR = max(maxR, height[r])
            r -= 1

    return units

if __name__ == '__main__':

    case1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    case2 = [4,2,0,3,2,5]

    print(trap(case1))
    print(trap(case2))
