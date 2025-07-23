# https://leetcode.com/problems/cinema-seat-allocation/description/

from typing import List


def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:

    for row in range(n):
        for col in range(10):
            for res_seat in reservedSeats:
                pass


if __name__ == '__main__':
    case1 = 3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    case2 = 2, [[2,1],[1,8],[2,6]]
    case3 = 4, [[4,3],[1,4],[4,6],[1,7]]

    print(maxNumberOfFamilies(*case1))
    print(maxNumberOfFamilies(*case2))
    print(maxNumberOfFamilies(*case3))
