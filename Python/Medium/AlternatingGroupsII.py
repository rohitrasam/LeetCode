# https://leetcode.com/problems/alternating-groups-ii/description/?envType=problem-list-v2&envId=sliding-window


from typing import List


def numberOfAlternatingGroups(colors: List[int], k: int) -> int:
    # colors += colors[:k-1]
    # n = len(colors)
    # res = 0
    # l = 0
    # r = 1
    # while r < n:
    #     if colors[r] == colors[r-1]:
    #         l = r
    #         r += 1
    #         continue
            
    #     r += 1
    #     if r - l < k:
    #         continue
        
    #     res += 1
    #     l += 1
    
    # return res

    n = len(colors)
    res = 0
    alter_count = 1
    last_color = colors[0]
    for i in range(1, n + k - 1):
        idx = i % n
        if colors[idx] == last_color:
            alter_count = 1
            last_color = colors[idx]
            continue

        alter_count += 1
        if alter_count >= k:
            res += 1
            
        last_color = colors[idx]

    return res

if __name__ == '__main__':

        case = [0,1,0,1,0], 3
        print(numberOfAlternatingGroups(*case))
        case = [0,1,0,0,1,0,1], 6
        print(numberOfAlternatingGroups(*case))
        case = [1,1,0,1], 4
        print(numberOfAlternatingGroups(*case))
