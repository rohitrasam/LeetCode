from typing import List


def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    alice_total = sum(aliceSizes)
    bob_total = sum(bobSizes)
    diff = (alice_total - bob_total) // 2
    b_set = set(bobSizes)

    for i in aliceSizes:
        if i - diff in b_set:
            return [i, i-diff]

    return [0, 0]


if __name__ == '__main__':

    case1 = [1, 1], [2, 2]
    case2 = [1, 2], [2, 3]
    case3 = [2], [1, 3]

    print(fairCandySwap(case1))
    print(fairCandySwap(case2))
    print(fairCandySwap(case3))
