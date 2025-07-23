# https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=daily-question&envId=2025-01-01

def maxScore(s: str) -> int:

    maxCount = 0
    left = right = 0
    # for i in range(1, len(s)):
    #     counter = 0
    #     for z in s[:i]:
    #         if z == "0":
    #             counter += 1
        
    #     for o in s[i:]:
    #         if o == "1":
    #             counter += 1

    #     maxCount = max(counter, maxCount)

    for char in s:
        right += 1 if char == "1" else 0
    
    for char in s[:len(s)-1]:
        left += 1 if char == "0" else 0
        right += 0 if char =="0" else -1
        maxCount = max(left + right, maxCount)

    return maxCount

if __name__ == '__main__':

    case1 = "011101"
    case2 = "00111"
    case3 = "1111"
    case4 = "10001"
    print(maxScore(case1))
    print(maxScore(case2))
    print(maxScore(case3))
    print(maxScore(case4))