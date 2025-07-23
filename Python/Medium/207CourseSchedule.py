# https://leetcode.com/problems/course-schedule/description/


from collections import defaultdict, deque
from typing import DefaultDict, Dict, List, Set


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    
    # preMap: Dict[int, List[int]] = {i: [] for i in range(numCourses)}
    preMap: DefaultDict[int, List[int]] = defaultdict(list)

    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    visited: Set[int] = set()

    def dfs(node: int) -> bool:
        if node in visited:
            return False
        if len(preMap[node]) == 0:
            return True
        
        visited.add(node)

        for pre in preMap[node]:
            if not dfs(pre):
                return False

        visited.remove(node)
        preMap[node] = []

        return True
    
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    
    return True

if __name__ == '__main__':
    case = 2, [[1,0]]
    print(canFinish(*case))
    case = 2, [[1,0],[0,1]]
    print(canFinish(*case))
    case = 5, [[1,0],[2,0],[1,3],[1,4],[3,4]]
    print(canFinish(*case))