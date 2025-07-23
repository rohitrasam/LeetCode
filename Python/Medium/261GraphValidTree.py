# https://neetcode.io/problems/valid-tree?list=blind75


from collections import defaultdict
from typing import DefaultDict, List, Set


def validTree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) > n - 1:
        return False
    
    visited: Set[int] = set()
    adj: DefaultDict[int, List[int]] =  defaultdict(list)

    for src, end in edges:
        adj[src].append(end)
        adj[end].append(src)

    def dfs(node: int, prev: int) -> bool:
        if node in visited:
            return False
        
        visited.add(node)
        for nei in adj[node]:
            if nei == prev:
                continue
            if not dfs(nei, node):
                return False
        
        return True

    return dfs(0, -1) and len(visited) == n

if __name__ == '__main__':
    case = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(validTree(*case))

    case = 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(validTree(*case))