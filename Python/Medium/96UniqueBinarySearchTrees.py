# https://leetcode.com/problems/unique-binary-search-trees/description/?envType=problem-list-v2&envId=tree

from typing import List


def numTrees(n: int) -> int:
    
    # numTree[4] = numTree[0] * numTree[3] + 
    #              numTree[1] * numTree[2] +
    #              numTree[2] * numTree[1] +
    #              numTree[3] * numTree[0]

    numTree: List[int] = [1] * (n+1)

    # 0 node = 1 tree
    # 1 node = 1 tree

    for nodes in range(2, n+1):
        total = 0
        for root in range(1, nodes+1):
            left = root-1
            right = nodes - root
            total += numTree[left] * numTree[right]
        numTree[nodes] = total
    
    return numTree[n]

if __name__ == '__main__':

    case = 5
    print(f"{case = } -> {(numTrees(case))}")
    case = 4
    print(f"{case = } -> {(numTrees(case))}")
    case = 3
    print(f"{case = } -> {(numTrees(case))}")
    case = 1
    print(f"{case = } -> {(numTrees(case))}")