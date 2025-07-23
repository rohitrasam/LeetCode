# https://leetcode.com/problems/find-eventual-safe-states/description/?envType=daily-question&envId=2025-01-24


from typing import List


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    safe: dict[int, bool] = {}

    def dfs(i: int):
        if i in safe:
            return safe[i]
        safe[i] = False
        for ne in graph[i]:
            if not dfs(ne):
                return safe[i]
    
        safe[i] = True
        return safe[i]
    

    res = []
    for i in range(n):
        if dfs(i):
            res.append(i)
    return res

        
if __name__ == '__main__':

    case1 = [[1,2],[2,3],[5],[0],[5],[],[]]
    case2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    case3 = [[1,2,5],[],[3,4,5],[4],[5],[]]


    print(eventualSafeNodes(case1))
    print(eventualSafeNodes(case2))
    print(eventualSafeNodes(case3))