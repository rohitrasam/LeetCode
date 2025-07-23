# https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-05

from typing import List

def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    
    s = list(s)
    n = len(s)
    diff = [0] * len(s)

    for start, end, d in shifts:
        if d:
            diff[start] += 1
            if end + 1 < n:
                diff[end+1] -= 1
        else:
            diff[start] -= 1
            if end + 1 < n:
                diff[end+1] += 1
    
    numShifts = 0
    a = ord('a')
    for i in range(len(s)):
        numShifts = (diff[i] + numShifts) % 26
        s[i] = chr(a + (ord(s[i]) - a + numShifts) % 26)

            
    return ''.join(s)


if __name__ == '__main__':
    case1 = "abc", [[0,1,0],[1,2,1],[0,2,1]]
    case2 = "dztz", [[0,0,0],[1,1,1]]

    print(shiftingLetters(*case1))
    print(shiftingLetters(*case2))
