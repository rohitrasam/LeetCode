from typing import List


def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    s_ptr = g_ptr = 0

    while s_ptr < len(s) and g_ptr < len(g):
        if s[s_ptr] >= g[g_ptr]:
            s_ptr += 1
            g_ptr += 1
        else:
            s_ptr += 1
                
    return g_ptr


if __name__ == '__main__':

    case1 = [1, 2, 3], [1, 1]
    case2 = [1, 2], [1, 2, 3]
    case3 = [1, 2, 1, 4, 5, 2], [5, 1, 2, 10]

    print(findContentChildren(*case1))
    print(findContentChildren(*case2))
    print(findContentChildren(*case3))

