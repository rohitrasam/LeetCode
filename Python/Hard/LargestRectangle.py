from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea

if __name__ == '__main__':

    case1 = [2,1,5,6,2,3]
    case2 = [2,4]

    print(largestRectangleArea(case1))
    print(largestRectangleArea(case2))
