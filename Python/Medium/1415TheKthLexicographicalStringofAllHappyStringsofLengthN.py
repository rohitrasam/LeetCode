# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=problem-list-v2&envId=backtracking


from typing import List, Tuple

"""
n = 3,
ans = ["", "abc", "aba"]
1. dfs
    string = []
    count = 0
    idx = 0
    2. dfs
        string = [a]
        count = 1
        idx = 1
        3. dfs
            string = [a, b]
            count = 2
            idx = 2
            4. dfs
                string = [a, b, c]
                count = 3
                idx = 3
            5. dfs
                string = [a, b, a]
                count = 3
                idx = 0
        
"""
    

def getHappyString(n: int, k: int) -> str:
    """ My Solution - Failed """
    # ans: List[str] = [""]
    # alpha: List[str] = ['a', 'b', 'c']

    # def dfs(string: List[str], count: int, idx: int) -> None:
    #     if string and string[-1] == alpha[idx]:
    #         return
    #     if count >= n:
    #         ans.append("".join(string))
    #         return
        
    #     string.append(alpha[idx])
    #     dfs(string, count + 1, (idx + 1)%3)
        
    #     string.pop()
    #     dfs(string, count, (idx + 2) % 3)

    # dfs([], 0, 0)
    # ans.sort()

    # return ans[k]

    """ Leetcode Editorial Soultion """
    ans: List[str] = [""]
    alpha: List[str] = ['a', 'b', 'c']

    def dfs(string: List[str]) -> None:

        if len(string) >= n:
            ans.append("".join(string))
            return
        
        for char in alpha:
            if string and string[-1] == char:
                continue
            string.append(char)
            dfs(string)
            string.pop()

    dfs([])
    
    return ans[k] if len(ans)-1 >= k else ans[0]
    

if __name__ == '__main__':

    # case: Tuple[int] = 1, 3
    # print(getHappyString(*case))
    # case: Tuple[int] = 1, 4
    # print(getHappyString(*case))
    case: Tuple[int] = 3, 9
    print(getHappyString(*case))
    case: Tuple[int] = 2, 3
    print(getHappyString(*case))
