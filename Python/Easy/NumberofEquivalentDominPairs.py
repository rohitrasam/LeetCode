# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=problem-list-v2&envId=hash-table


from typing import Dict, List


def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    # counter: Dict[List, int] = {}
    # pairs = 0
    # for domino in dominoes:
    #     if (domino[0], domino[1]) in counter: 
    #         counter[(domino[0], domino[1])] += 1
    #         pairs += counter[(domino[0], domino[1])]
    #     elif (domino[1], domino[0]) in counter:
    #         counter[(domino[1], domino[0])] += 1
    #         pairs += counter[(domino[1], domino[0])]
    #     else:
    #         counter[tuple(domino)] = 0
    
    # return pairs

    counter: Dict[List, int] = {}
    pairs = 0

    for a, b in dominoes:
        if a > b:
            a, b = b, a
        key = a * 2 + b
        if key in counter:
            counter[key] += 1
            pairs += counter[key]
        else:
            counter[key] = 0
    return pairs


if __name__ == '__main__':

    case = [[1,2],[2,1],[3,4],[5,6]]
    print(numEquivDominoPairs(case))
    case = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    print(numEquivDominoPairs(case))
