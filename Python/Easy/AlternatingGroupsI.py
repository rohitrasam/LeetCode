# https://leetcode.com/problems/alternating-groups-i/description/?envType=problem-list-v2&envId=sliding-window



from typing import List


def numberOfAlternatingGroups(colors: List[int]) -> int:
    n = len(colors)
    count = 0
    for l in range(n):
        r = (l + 2)%n
        if colors[l] != colors[(l+1)%n] and colors[(r-1)%n] != colors[r]:
            count += 1
    
    return count


if __name__ == '__main__':


    case = [1,1,1]
    print(numberOfAlternatingGroups(case))
    case = [0,1,0,0,1]
    print(numberOfAlternatingGroups(case))
    case = [0,1,0,1,0,1,0,1,1,1,0,1]
    print(numberOfAlternatingGroups(case))
