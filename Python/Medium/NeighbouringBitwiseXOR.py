# https://leetcode.com/problems/neighboring-bitwise-xor/description/?envType=daily-question&envId=2025-01-17


from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:

    n = len(derived)
    og0 = [0] * n
    og1 = [1] * n

    for idx in range(len(derived)):
        if idx != n-1:
            og0[idx+1] = og0[idx] ^ derived[idx]
            og1[idx+1] = og1[idx] ^ derived[idx]

    return og0[n-1] ^ og0[0] == derived[n-1] or og1[n-1] ^ og1[0] == derived[n-1]
    


if __name__ == '__main__':

    case1 = [1,1,0]
    case2 = [1,1]
    case3 = [1,0]

    print(doesValidArrayExist(case1))
    print(doesValidArrayExist(case2))
    print(doesValidArrayExist(case3))
