# https://leetcode.com/problems/course-schedule-ii/description/



from collections import defaultdict
from typing import DefaultDict, List, Set


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    graph: DefaultDict[int, List[int]] = defaultdict(list)
    for crs, pre in prerequisites:
        graph[pre].append(crs)

    stack: List[int] = []
    visited: Set[int] = set()
    cycle: Set[int] = set()

    def dfs(curr_crs: int) -> bool:
        if curr_crs in cycle:
            return False
        if curr_crs in visited:
            return True
        
        cycle.add(curr_crs)
        for crs in graph[curr_crs]:
            if dfs(crs) == False:
                return False
            
        cycle.remove(curr_crs)
        visited.add(curr_crs)
        stack.append(curr_crs)
        return True
    
    for node in range(numCourses):
        if dfs(node) == False:
            return []
    
    return stack[::-1]


if __name__ == '__main__':

    case = 2, [[1,0]]
    print(findOrder(*case))
    case = 4, [[1,0],[2,0],[3,1],[3,2]]
    print(findOrder(*case))
    case = 1, []
    print(findOrder(*case))
    case = 6, [[3,0],[3,1],[2,1],[4,3],[5,4],[5,2]]
    print(findOrder(*case))
