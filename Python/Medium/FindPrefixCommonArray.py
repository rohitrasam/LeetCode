# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2025-01-14

from typing import List


def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:

    res = []

    elemInA = set()
    elemInB = set()

    for i in range(len(A)):
        elemInA.add(A[i])
        elemInB.add(B[i])

        common = 0
        for elem in elemInA:
            if elem in elemInB:
                common += 1

        res.append(common)        

    # for i in range(len(A)):
    #     common = 0
    #     for j in range(i+1):
    #         for k in range(i+1):
    #             if A[j] == B[k]:
    #                 common += 1
    #     res.append(common)

    return res

if __name__ == '__main__':

    case1 = [1,3,2,4], [3,1,2,4]
    case2 = [2,3,1], [3,1,2]

    print(findThePrefixCommonArray(*case1))
    print(findThePrefixCommonArray(*case2))