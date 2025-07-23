# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/?envType=problem-list-v2&envId=backtracking


from typing import List


def validStrings(n: int) -> List[str]:
    
    res = []

    def dfs(idx: int, bs: str, cur: str) -> None:
        if idx == n:
            res.append(bs)
            return

        # if bs and bs[-1] == cur == '0':
        #     return
        
        dfs(idx+1, bs+cur, '1')
        if bs and bs[-1] == '1':
            dfs(idx+1, bs+cur, '0')

    dfs(0, '', '0')
    dfs(0, '', '1')
    return res

if __name__ == '__main__':

    case = 5
    print(validStrings(case))
    case = 3
    print(validStrings(case))
    case = 1
    print(validStrings(case))