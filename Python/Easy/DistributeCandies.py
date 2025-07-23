from typing import List


def distributeCandies(candyType: List[int]) -> int:
    unique_types = set(candyType)
    return int(min(len(candyType) / 2, len(unique_types)))


if __name__ == '__main__':
    case1 = [1,1,2,2,3,3]
    case2 = [1,1,2,3]
    case3 = [6,6,6,6]

    print(distributeCandies(case1))
    print(distributeCandies(case2))
    print(distributeCandies(case3))
