# https://leetcode.com/problems/defuse-the-bomb/description/?envType=problem-list-v2&envId=sliding-window

from typing import List


def decrypt(code: List[int], k: int) -> List[int]:
    # n = len(code)
    # res = [0] * n
    # if k > 0:
    #     for i in range(len(code)):
    #         for j in range(i+1, i+k+1):
    #             res[i] += code[j % n]
    # elif k < 0:
    #     for i in range(len(code)):
    #         for j in range(i-1, i+k-1, -1):
    #             res[i] += code[j % n]

    # return res
    n = len(code)
    res = [0] * n
    if k == 0:
        return res
    
    start, end, win = 1, k, 0

    if k < 0:
        start = n - abs(k)
        end = n - 1

    for i in range(start, end + 1):
        win += code[i]

    for i in range(n):
        res[i] = win
        win -= code[start % n]
        win += code[(end + 1) % n]
        start += 1
        end += 1
    
    return res


if __name__ == '__main__':

    case = [5,7,1,4], 3
    print(decrypt(*case))
    case = [1,2,3,4], 0
    print(decrypt(*case))
    case = [2,4,9,3], -2
    print(decrypt(*case))