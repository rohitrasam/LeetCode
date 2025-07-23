from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    count = [0] * len(nums)
    for num in nums:
        count[num-1] += 1
    
    out = []
    for i in range(len(count)):
        if count[i] == 0:
            out.append(i+1)

    return out

if __name__ == '__main__':

    case1 = [4,3,2,7,8,2,3,1]
    case2 = [1,1]

    print(findDisappearedNumbers(case1))
    print(findDisappearedNumbers(case2))