from typing import List

def findShortestSubArray(nums: List[int]) -> int:
    counter = {}

    for idx, num in enumerate(nums):
        high = -1
        if num in counter:
            counter[num][0] += 1
            counter[num][2] = max(high, idx)
        else:
            counter[num] = [1, idx, 0]
    
    max_occ = counter[max(counter, key=lambda x: counter[x][0])][0]
    ans = len(nums)
    for num in counter:
        if counter[num][0] == max_occ:
            ans = min(ans, abs(counter[num][2] - counter[num][1]))
        
    return ans+1
            


if __name__ == '__main__':

    # case1 = [1, 2, 2, 3, 1]
    # case2 = [1,2,2,3,1,4,2]
    case2 = [1]
    # print(findShortestSubArray(case1))
    print(findShortestSubArray(case2))